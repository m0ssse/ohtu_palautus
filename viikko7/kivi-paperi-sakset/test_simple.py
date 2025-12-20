#!/usr/bin/env python3
"""Simple manual test using urllib to test the web app"""
import urllib.request
import urllib.parse
from http.cookiejar import CookieJar

def test_home_page():
    print("Testing home page...")
    response = urllib.request.urlopen("http://127.0.0.1:5000/")
    html = response.read().decode('utf-8')
    assert "Kivi-Paperi-Sakset" in html, "Home page title not found"
    assert "Pelaaja vs Pelaaja" in html, "Game mode option not found"
    print("✓ Home page loads correctly")

def test_game_flow():
    print("\nTesting game flow with cookies...")
    
    # Create cookie jar
    cookie_jar = CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
    urllib.request.install_opener(opener)
    
    # Start a game
    print("  - Starting Player vs AI game...")
    data = urllib.parse.urlencode({"game_type": "b"}).encode()
    req = urllib.request.Request("http://127.0.0.1:5000/new-game", data=data)
    response = urllib.request.urlopen(req)
    
    # Get play page
    print("  - Loading play page...")
    response = urllib.request.urlopen("http://127.0.0.1:5000/play")
    html = response.read().decode('utf-8')
    assert "Tekoäly" in html, "AI game mode not shown"
    print("✓ Play page loads for AI mode")
    
    # Make a move
    print("  - Making a move (Rock)...")
    data = urllib.parse.urlencode({"move": "k"}).encode()
    req = urllib.request.Request("http://127.0.0.1:5000/make-move", data=data)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    assert "Pelitilanne" in html, "Game state not shown"
    print("✓ Move executed successfully")
    
    # Play another round
    print("  - Playing another round...")
    response = urllib.request.urlopen("http://127.0.0.1:5000/play")
    data = urllib.parse.urlencode({"move": "p"}).encode()
    req = urllib.request.Request("http://127.0.0.1:5000/make-move", data=data)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    print("✓ Second round completed")

if __name__ == "__main__":
    print("="* 60)
    print("Testing Rock-Paper-Scissors Web Application")
    print("="* 60)
    
    try:
        test_home_page()
        test_game_flow()
        print("\n" + "=" * 60)
        print("✅ All tests passed successfully!")
        print("=" * 60)
        print("\nThe web application is working correctly.")
        print("You can access it at: http://127.0.0.1:5000")
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
