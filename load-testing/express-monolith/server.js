const express = require("express");
const app = express();
const port = 3001;

// Function to simulate a delay
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

// Route 1
app.get("/route1", async (req, res) => {
    await sleep(1000);
    res.json({ message: "Response from Route 1" });
});

// // Route 2
// app.get("/route2", async (req, res) => {
//     await sleep(2000);
//     res.json({ message: "Response from Route 2" });
// });

// // Route 3
// app.get("/route3", async (req, res) => {
//     await sleep(3000);
//     res.json({ message: "Response from Route 3" });
// });

// Start the server
app.listen(port, () => {
    console.log(`Express app listening at http://localhost:${port}`);
});
