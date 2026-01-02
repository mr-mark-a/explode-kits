# Explo-Cats Card Game 🐱💣

A multiplayer card game inspired by Exploding Kittens, built with Node.js, Express, and Socket.IO.

## 🎮 Game Features

- **Multiplayer**: Host/Join games with room codes
- **Card Types**:
  - 💣 Exploding Kitten - Draw and explode!
  - 🛡️ Defuse - Save yourself from explosion
  - 🚫 Nope - Cancel actions
  - 🧔 Beard Cat, 📯 Hringg, 🌮 Tacocat - Combo cards
  - ⏭️ Skip, ⚔️ Attack, 🔀 Shuffle, 🔮 See Future

## 🚀 Quick Start

### Local Development

1. **Install dependencies:**
   ```bash
   cd explo-cats/server
   npm install
   ```

2. **Start server:**
   ```bash
   npm start
   ```

3. **Open game:**
   - Navigate to `http://localhost:3000/front-end.html`

### Deploy to Render.com (Free)

1. Push this repository to GitHub
2. Go to [Render.com](https://render.com/)
3. Create new Web Service
4. Configure:
   - **Root Directory:** `explo-cats/server`
   - **Build Command:** `npm install`
   - **Start Command:** `node back-end.js`
   - **Plan:** Free

## 📁 Project Structure

```
explode-kits/
├── explo-cats/
│   ├── front-end.html      # Game UI
│   └── server/
│       ├── back-end.js     # Game server
│       ├── package.json    # Dependencies
│       └── .gitignore      # Git ignore rules
└── README.md
```

## 🎯 How to Play

1. One player hosts a game and shares the room code
2. Other players join using the code
3. Each player starts with 5 cards (including 1 Defuse)
4. Take turns drawing cards
5. Avoid the Exploding Kitten or use a Defuse!
6. Last player alive wins!

## 🛠️ Technology Stack

- **Backend:** Node.js, Express, Socket.IO
- **Frontend:** HTML5, CSS3, JavaScript
- **Real-time:** WebSocket communication

## 📝 License

MIT License - Feel free to use and modify!
