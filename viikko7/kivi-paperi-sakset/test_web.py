"""Test script to verify the web application game modes work correctly"""
import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def test_player_vs_player():
    print("Testing Player vs Player mode...")
    session = requests.Session()
    
    # Start game
    response = session.post(f"{BASE_URL}/new-game", data={"game_type": "a"}, allow_redirects=False)
    assert response.status_code == 302
    
    # Get play page
    response = session.get(f"{BASE_URL}/play")
    assert response.status_code == 200
    assert "Pelaaja vs Pelaaja" in response.text
    
    # Make a move
    response = session.post(f"{BASE_URL}/make-move", data={"move": "k", "player2_move": "s"})
    assert response.status_code == 200
    assert "Kivi" in response.text
    assert "Sakset" in response.text
    
    print("✓ Player vs Player mode works!")
    return True

def test_player_vs_ai():
    print("Testing Player vs AI mode...")
    session = requests.Session()
    
    # Start game
    response = session.post(f"{BASE_URL}/new-game", data={"game_type": "b"}, allow_redirects=False)
    assert response.status_code == 302
    
    # Get play page
    response = session.get(f"{BASE_URL}/play")
    assert response.status_code == 200
    assert "Tekoäly" in response.text
    
    # Make a move
    response = session.post(f"{BASE_URL}/make-move", data={"move": "p"})
    assert response.status_code == 200
    
    print("✓ Player vs AI mode works!")
    return True

def test_player_vs_advanced_ai():
    print("Testing Player vs Advanced AI mode...")
    session = requests.Session()
    
    # Start game
    response = session.post(f"{BASE_URL}/new-game", data={"game_type": "c"}, allow_redirects=False)
    assert response.status_code == 302
    
    # Get play page
    response = session.get(f"{BASE_URL}/play")
    assert response.status_code == 200
    assert "Parannettu" in response.text
    
    # Make a move
    response = session.post(f"{BASE_URL}/make-move", data={"move": "s"})
    assert response.status_code == 200
    
    # Make another move to test AI memory
    response = session.get(f"{BASE_URL}/play")
    response = session.post(f"{BASE_URL}/make-move", data={"move": "k"})
    assert response.status_code == 200
    
    print("✓ Player vs Advanced AI mode works!")
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("Testing Rock-Paper-Scissors Web Application")
    print("=" * 50)
    
    try:
        test_player_vs_player()
        test_player_vs_ai()
        test_player_vs_advanced_ai()
        print("\n" + "=" * 50)
        print("✅ All tests passed!")
        print("=" * 50)
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
