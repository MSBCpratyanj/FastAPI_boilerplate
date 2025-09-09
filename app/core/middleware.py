from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import logging
from logging.handlers import RotatingFileHandler
import os
import json
import time
from typing import Any, Dict
from fastapi import HTTPException
from fastapi.responses import JSONResponse

# --- Setup logger (file + console) ---
os.makedirs("logs", exist_ok=True)
log_file = "logs/api.log"

logger = logging.getLogger("api-logger")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s | LEVEL: %(levelname)s | %(message)s")

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

file_handler = RotatingFileHandler(
    log_file, maxBytes=5*1024*1024, backupCount=5, encoding="utf-8"
)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

# --- Sensitive fields ---
SENSITIVE_KEYS = {"password", "token", "secret", "authorization"}


def mask_sensitive(data: Any) -> Any:
    if isinstance(data, dict):
        return {
            k: ("***" if k.lower() in SENSITIVE_KEYS else mask_sensitive(v))
            for k, v in data.items()
        }
    elif isinstance(data, list):
        return [mask_sensitive(i) for i in data]
    return data


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        client_ip = request.client.host if request.client else "unknown"

        try:
            body_bytes = await request.body()
            body = body_bytes.decode("utf-8")
            try:
                parsed_body = mask_sensitive(json.loads(body))
            except Exception:
                parsed_body = body[:500]
        except Exception:
            parsed_body = None

        headers = {
            k: ("***" if k.lower() in SENSITIVE_KEYS else v)
            for k, v in dict(request.headers).items()
            if k.lower() in {"content-type", "user-agent", "authorization"}
        }

        
        try:
            response = await call_next(request)
            process_time = (time.time() - start_time) * 1000
            response_body = b""
            async for chunk in response.body_iterator:
                response_body += chunk

            response = Response(
                content=response_body,
                status_code=response.status_code,
                headers=dict(response.headers),
                media_type=response.media_type,
            )

            try:
                body_str = response_body.decode("utf-8")
                parsed_response = mask_sensitive(json.loads(body_str))
            except Exception:
                parsed_response = body_str[:500] if body_str else None

        except Exception as e:
            # ✅ If the route raises an exception, catch it here
            process_time = (time.time() - start_time) * 1000
            parsed_response = {"error": str(e)}
            response = JSONResponse(content=parsed_response, status_code=500)

            # --- Build log line ---
            log_line = (
                f"client_ip={client_ip} | "
                f"method={request.method} | "
                f"path={request.url.path} | "
                f"query_params={dict(request.query_params)} | "
                f"headers={headers} | "
                f"request_body={parsed_body} | "
                f"status_code={response.status_code} | "
                f"response_time_ms={round(process_time, 2)} | "
                f"response_body={parsed_response}"
            )

            if response.status_code >= 500:
                logger.error(log_line)
            elif response.status_code >= 400:
                logger.warning(log_line)
            else:
                logger.info(log_line)

            return response
        return response