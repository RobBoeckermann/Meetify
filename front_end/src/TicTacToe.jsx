import React from 'react';
import './TicTacToe.css';

const BOARD_SIZE = 9;
const PIECES = ['X', 'O'];

function Square(props) {
  return (
    <button className="square" onClick={props.onClick}>
      {props.value}
    </button>
  );
}

class Board extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      squares: Array(BOARD_SIZE).fill(null),
      nextPiece: 'X'
    };
  }

  handleClick(i) {
    // If someone won, reset the board on click
    const winner = calculateWinner(this.state.squares);
    if (winner) {
      const emptySquares = Array(BOARD_SIZE).fill(null);
      const loserPiece = winner == 'O' ? 'X' : 'O';
      this.setState({squares: emptySquares, nextPiece: loserPiece});
      return;
    }

    const squares= this.state.squares.slice();
    squares[i] = this.state.nextPiece;

    console.log(squares);

    const nextPiece = this.state.nextPiece == 'O' ? 'X' : 'O';

    this.setState({squares, nextPiece});
  }

  renderSquare(i) {
    return (
      <Square
        value={this.state.squares[i]}
        onClick={() => this.handleClick(i)}
      />
    );
  }

  renderSquares(min, max) {
    let val = min;
    let retList = [];
    while (val <= max) {
      retList.push(this.renderSquare(val));
      val += 1;
    }
    return retList;
  }

  render() {
    const winner = calculateWinner(this.state.squares);

    let status;
    if (winner) {
      status = `WINNER: ${winner}`;
    } else {
      status = `Next player: ${this.state.nextPiece}`;
    }

    return (
      <div>
        <div className="status">{status}</div>
        <div className="board-row">
          {this.renderSquares(0, 2)}
        </div>
        <div className="board-row">
          {this.renderSquares(3, 5)}
        </div>
        <div className="board-row">
          {this.renderSquares(6, 8)}
        </div>
      </div>
    );
  }
}

export class Game extends React.Component {
  render() {
    return (
      <div className="game">
        <div className="game-board">
          <Board />
        </div>
        <div className="game-info">
          <div>{/* status */}</div>
          <ol>{/* TODO */}</ol>
        </div>
      </div>
    );
  }
}

// -- UTIL FUNCTIONS --

function calculateWinner(squares) {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];
  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null;
}
