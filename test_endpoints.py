from starlette.testclient import TestClient
from app.main import app

client = TestClient(app)

def run_tests():
    # 1. Test Home page
    r_home = client.get('/')
    assert r_home.status_code == 200, f'Home failed: {r_home.status_code}'

    # 2. Test Login
    r_login = client.post('/api/auth/login', json={'email': 'demo@meditrack.bd', 'password': 'password123'})
    assert r_login.status_code == 200, f'Login failed: {r_login.text}'
    token = r_login.json()['access_token']
    headers = {'Authorization': f'Bearer {token}'}

    # 3. Test Family members
    r_fam = client.get('/api/family', headers=headers)
    assert r_fam.status_code == 200, f'Family failed: {r_fam.text}'
    members = r_fam.json()
    assert len(members) >= 2, f'Expected family members, got: {len(members)}'
    print(f"Family members found: {len(members)}")

    # 4. Test Timeline for Father
    father = next(m for m in members if 'Abdul' in m['name'] or 'Father' in m['relationship'])
    f_id = father['id']
    r_time = client.get(f'/api/tracking/timeline?member_id={f_id}', headers=headers)
    assert r_time.status_code == 200
    timeline_data = r_time.json()
    print('Father schedule summary:', timeline_data['summary'])

    # 5. Test Dose check-off (Taken)
    slots = timeline_data['timeline']
    if 'morning' in slots and len(slots['morning']) > 0:
        first_dose = slots['morning'][0]
        r_log = client.post('/api/tracking/log', json={
            'medication_id': first_dose['medication_id'],
            'member_id': f_id,
            'dose_date': timeline_data['date'],
            'slot': 'morning',
            'status': 'taken'
        }, headers=headers)
        assert r_log.status_code == 200
        print('Dose logged successfully as TAKEN:', r_log.json())

    # 6. Test Doctor directory
    r_doc = client.get('/api/doctors?division=Dhaka&area=Dhanmondi')
    assert r_doc.status_code == 200
    docs = r_doc.json()
    assert len(docs) >= 1
    print('Found doctors in Dhanmondi:', [d['name'] for d in docs])

    # 7. Test Admin Login & Stats
    r_adm_login = client.post('/api/auth/login', json={'email': 'admin@meditrack.bd', 'password': 'admin123'})
    adm_token = r_adm_login.json()['access_token']
    r_stats = client.get('/api/admin/stats', headers={'Authorization': f'Bearer {adm_token}'})
    assert r_stats.status_code == 200
    print('Admin stats:', r_stats.json())

    # 8. Test all HTML pages render without Jinja errors
    pages = ['/', '/login', '/register', '/dashboard', '/medications', '/doctors', '/appointments', '/prescriptions', '/family']
    for p in pages:
        r = client.get(p, headers=headers)
        assert r.status_code in [200, 302], f'Page {p} failed: {r.status_code}'
        print(f'Page {p}: OK ({r.status_code})')

    r_adm_page = client.get('/admin', headers={'Authorization': f'Bearer {adm_token}'})
    assert r_adm_page.status_code == 200
    print('Page /admin: OK (200)')

    print('ALL ENDPOINTS & TEMPLATES RENDER 100% CLEANLY!')

if __name__ == '__main__':
    run_tests()
