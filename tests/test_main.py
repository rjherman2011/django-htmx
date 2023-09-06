
def test_read_main(client):
    response = client.get("/")
    assert response.status_code == 200
    assert """<h2 class="text-2xl leading-relaxed text-slate-800 uppercase">Welcome</h2>""" in response.text
