import main


def test_index():
    main.app.testing = True
    client = main.app.test_client()

    r = client.get('/')
    assert r.status_code == 200
    assert 'Welcome to Google App Engine! Thank you Prof Gao for teaching Cloud Technologies ' in r.data.decode('utf-8')
