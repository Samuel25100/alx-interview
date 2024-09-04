#!/usr/bin/node
const request = require('request');
const num = process.argv[2];

function fetchData(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        return reject(error);
      }
      if (response.statusCode !== 200) {
        return reject(new Error('Failed with status ' + response.statusCode));
      }
      resolve(body);
    });
  });
}

async function parser() {
	const body = await fetchData(`https://swapi-api.alx-tools.com/api/films/${num}`);
	const data = JSON.parse(body)
	for (const line of data["characters"]) {
		const body1 = await fetchData(line);
		const data1 = JSON.parse(body1);
		console.log(data1['name']);
	}
}

parser()
