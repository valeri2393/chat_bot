FROM python:3.10-slim
ENV TOKEN="6740181603:AAGBqp-b3SRyifB8Vt2VnhgALAHE10oTfgA"
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "new_bot.py"]
