import os


BASE_PATH: str = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '..'
    )
)

SLACK_WEBHOOK_URL: str = os.getenv('SLACK_WEBHOOK_URL', 'https://hooks.slack.com/services/cobre-webhook-url')

NOTIFY_THRESHOLD: float = float(os.getenv('NOTIFY_THRESHOLD', '0.5'))

DATABASE_URI: str = os.getenv('DATABASE_URI')
