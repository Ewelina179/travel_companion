#!/bin/bash
cd backend
celery -A myproject worker -l info