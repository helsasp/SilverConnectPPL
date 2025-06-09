import axios from 'axios';

class AuthService {
  constructor() {
    this.api = axios.create({
      baseURL: 'http://localhost:3000/api/gateway',
    });
  }

  async signup(data) {
    return this.api.post('/auth/signup', data);
  }

  async login(credentials) {
    return this.api.post('/auth/login', credentials);
  }

  async forgotPassword(email) {
    return this.api.post('/auth/forgot-password', { email });
  }
}

export default AuthService;