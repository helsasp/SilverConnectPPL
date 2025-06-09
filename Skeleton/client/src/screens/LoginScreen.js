import React, { useContext, useState } from 'react';
import { View, Text, TextInput, Button } from 'react-native';
import { AuthContext } from '../contexts/AuthContext';
import { friendIterator } from '../utils/Iterator';

const LoginScreen = ({ navigation }) => {
  const { state, transitionState, authService } = useContext(AuthContext);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async () => {
    try {
      await authService.login({ email, password });
      transitionState('OnboardingState');
      navigation.navigate('Dashboard');
    } catch (error) {
      alert('Login failed');
    }
  };

  // Contoh Iterator untuk daftar teman (dummy data)
  const friends = ['John', 'Jane', 'Bob'];
  const friendIter = friendIterator(friends);
  const nextFriend = () => console.log(friendIter.next().value);

  return (
    <View>
      <Text>State: {state}</Text>
      <TextInput placeholder="Email" value={email} onChangeText={setEmail} />
      <TextInput placeholder="Password" value={password} onChangeText={setPassword} secureTextEntry />
      <Button title="Login" onPress={handleLogin} />
      <Button title="Next Friend" onPress={nextFriend} />
    </View>
  );
};

export default LoginScreen;