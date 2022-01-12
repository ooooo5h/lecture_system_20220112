from server import create_app

app = create_app()


# 향후 - 디버그모드/실제 서버모드 등등 구별 가능 구조
app.run(host='0.0.0.0')
