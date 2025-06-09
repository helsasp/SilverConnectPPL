const express = require('express');
const app = express();
app.use(express.json());

app.post('/auth/signup', (req, res) => {
  // Proxy ke auth_service
  res.send({ message: 'Signup routed' });
});

app.post('/auth/login', (req, res) => {
  // Proxy ke auth_service
  res.send({ message: 'Login routed' });
});

app.listen(3000, () => console.log('API Gateway running on port 3000'));