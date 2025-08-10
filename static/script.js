let board = [];
let currentPlayer = "X";
let winner = null;
let userChoice = null;
let isTerminal = false;

const boardElement = document.getElementById("board");
const resetButton = document.getElementById("reset-button");
const gameOptions = document.getElementById("game-options");
const turnStatus = document.getElementById("turn-status");
const currentPlayerElement = document.getElementById("current-player");

// Create the game board dynamically
function createBoard() {
    boardElement.innerHTML = ""; // Clear previous board
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            const cell = document.createElement("div");
            cell.className = "cell";
            cell.addEventListener("click", () => handleCellClick(i, j));
            boardElement.appendChild(cell);
        }
    }
}

// Handle when a user clicks a cell
function handleCellClick(i, j) {
    // Check if cell is already filled, game is over, or it's not user's turn
    if (board[i][j] !== null || winner !== null || isTerminal || currentPlayer !== userChoice) {
        return;
    }

    // Send the move to the backend
    fetch("/move", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ i, j })
    })
    .then(response => response.json())
    .then(data => {
        board = data.board;
        currentPlayer = data.current_player;
        winner = data.winner;
        isTerminal = data.is_terminal;
        updateBoard();
    })
    .catch(error => {
        console.error('Error making move:', error);
    });
}

// Update the board UI
function updateBoard() {
    const cells = boardElement.getElementsByClassName("cell");
    let idx = 0;
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            cells[idx].textContent = board[i][j] === null ? "" : board[i][j];
            idx++;
        }
    }

    // Display the winner or whose turn it is
    if (winner) {
        turnStatus.textContent = `Game Over: ${winner} wins!`;
    } else if (isTerminal) {
        turnStatus.textContent = "Game Over: It's a tie!";
    } else {
        currentPlayerElement.textContent = currentPlayer;
        turnStatus.innerHTML = `Current Turn: <span id="current-player">${currentPlayer}</span>`;
    }
}

// Reset the game
function resetGame() {
    fetch("/reset")
        .then(response => response.json())
        .then(data => {
            board = data.board;
            currentPlayer = data.current_player;
            winner = null;
            userChoice = null; // Allow user to pick again
            isTerminal = false;
            gameOptions.style.display = "block";
            boardElement.style.display = "none";
            turnStatus.style.display = "none";
            resetButton.style.display = "none";
        })
        .catch(error => {
            console.error('Error resetting game:', error);
        });
}

// Set user's choice for X or O
function setUserChoice(choice) {
    userChoice = choice;
    fetch("/set_user_choice", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ choice })
    })
    .then(response => response.json())
    .then(data => {
        gameOptions.style.display = "none";
        boardElement.style.display = "grid";
        turnStatus.style.display = "block";
        resetButton.style.display = "block";
        createBoard(); // Ensure the board is created
        board = data.board;
        currentPlayer = data.current_player;
        userChoice = data.user_choice;
        winner = null;
        isTerminal = false;
        updateBoard();
    })
    .catch(error => {
        console.error('Error setting user choice:', error);
    });
}

// Add event listeners for X or O choice
document.getElementById("play-as-x").addEventListener("click", () => setUserChoice("X"));
document.getElementById("play-as-o").addEventListener("click", () => setUserChoice("O"));
resetButton.addEventListener("click", resetGame);

// Initialize the game options (prompt the user to pick X or O)
gameOptions.style.display = "block";