#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurence = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      occurence += 1;
    }
  }
  return occurence;
};
