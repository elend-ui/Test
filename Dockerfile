FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

# Install deps first (better layer caching)
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-install-project

# Then copy the rest of the project and install it
COPY . .
RUN uv sync --locked

# Put the venv's python first on PATH so it's discoverable
ENV PATH="/app/.venv/bin:$PATH"