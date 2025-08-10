# Tic Tac Toe Game

A web-based Tic Tac Toe game with an unbeatable AI opponent built using Flask and vanilla JavaScript. The AI uses the minimax algorithm to make optimal moves, ensuring it never loses.

## Features

- **Interactive Web Interface**: Clean, responsive design with clickable game board
- **Player Choice**: Choose to play as X or O
- **Unbeatable AI**: AI opponent uses minimax algorithm for optimal gameplay
- **Game State Management**: Proper turn handling and game termination detection
- **Reset Functionality**: Start new games without refreshing the page

## Project Structure

```
tic-tac-toe/
├── app.py              # Flask backend server
├── tictactoe.py        # Game logic and minimax AI
├── templates/
│   └── index.html      # Main HTML template
├── static/
│   ├── script.js       # Frontend JavaScript
│   └── style.css       # CSS styles (optional)
└── README.md           # Project documentation
```

## Installation

1. **Clone or download the project files**

2. **Install Python dependencies**:
   ```bash
   pip install flask
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

## How to Play

1. **Choose Your Symbol**: When the game starts, click either "Play as X" or "Play as O"
2. **Make Your Move**: Click on any empty cell on the 3x3 grid to place your symbol
3. **AI Response**: The AI will automatically make its move after yours
4. **Win Conditions**: Get three of your symbols in a row (horizontally, vertically, or diagonally)
5. **Reset Game**: Click "Reset Game" to start a new round

## Game Logic

### Core Components

- **`tictactoe.py`**: Contains all game logic including:
  - Board state management
  - Move validation
  - Win condition checking
  - Minimax algorithm implementation

- **`app.py`**: Flask backend that handles:
  - Game state persistence
  - HTTP API endpoints
  - Move processing and AI responses

- **Frontend**: JavaScript handles:
  - User interface updates
  - User input validation
  - Communication with backend

### AI Algorithm

The AI uses the **minimax algorithm** with the following characteristics:
- **Perfect Play**: The AI never makes a suboptimal move
- **Game Outcomes**: When playing optimally:
  - If you play as X (first), best outcome is a tie
  - If you play as O (second), best outcome is a tie
  - The AI will win if you make any mistakes

## API Endpoints

- **`GET /`**: Serves the main game page
- **`POST /move`**: Processes player moves and triggers AI response
- **`GET /reset`**: Resets the game to initial state
- **`POST /set_user_choice`**: Sets whether user plays as X or O

## Technical Details

### Game State Management

The game maintains state through:
- **Board representation**: 3x3 matrix with X, O, or None values
- **Turn calculation**: Dynamically determined based on move count
- **Terminal detection**: Checks for wins or draws after each move

### Frontend-Backend Communication

- Uses JSON for data exchange
- Asynchronous requests for smooth user experience
- Proper error handling and state synchronization

## Customization

You can extend the game by:
- Adding CSS styles in `static/style.css`
- Implementing difficulty levels
- Adding game statistics tracking
- Creating multiplayer functionality

## Dependencies

- **Python 3.x**
- **Flask**: Web framework for backend
- **Modern web browser**: For frontend functionality

## Troubleshooting

**Common Issues:**
- **Port already in use**: Change the port in `app.py` by modifying `app.run(port=5001)`
- **Module not found**: Ensure Flask is installed with `pip install flask`
- **JavaScript errors**: Check browser console for debugging information

## Contributing

Feel free to fork this project and submit pull requests for improvements such as:
- Enhanced UI/UX design
- Additional game modes
- Performance optimizations
- Code documentation improvements

## License

This project is open source and available under the MIT License.