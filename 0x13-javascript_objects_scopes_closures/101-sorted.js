#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new set(vals)];
const newDict = {};
for (const d in valsUniq) {
  const list = [];
  for (const y in totalist) {
    if (totalist[y][d] === valsUniq[j]) {
      list.unshift(totalist[y][0]);
    }
  }
  newDict[valsUniq[j]] = list;
}
console.log(newDict);

