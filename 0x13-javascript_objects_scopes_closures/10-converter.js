#!/usr/bin/node

exports.converter = function (base) {
  if (typeof base !== 'number' || base < 2 || base > 36) {
    throw new Error('base must be a number between 2 and 36');
  }
  return function (num) {
    if (typeof num !== 'number') {
      throw new Error('num must be a number');
    }
    return num.toString(base);
  };
};
