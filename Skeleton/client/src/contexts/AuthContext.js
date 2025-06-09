import React, { createContext, useState } from 'react';
import AuthService from '../services/AuthService';

export const AuthContext = createContext();

const AuthContextProvider = ({ children }) => {
  const [state, setState] = useState('SignupState'); // State awal

  const transitionState = (newState) => {
    setState(newState);
  };

  const authService = new AuthService();

  return (
    <AuthContext.Provider value={{ state, transitionState, authService }}>
      {children}
    </AuthContext.Provider>
  );
};

export default AuthContextProvider;