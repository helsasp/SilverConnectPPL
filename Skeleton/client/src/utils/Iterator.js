function friendIterator(friends) {
  let index = 0;
  const length = friends.length;

  return {
    next: () => {
      if (index < length) {
        return { value: friends[index++], done: false };
      }
      return { value: undefined, done: true };
    },
  };
}

export { friendIterator };