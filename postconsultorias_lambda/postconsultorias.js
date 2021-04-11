'use strict'
const AWS = require('aws-sdk');

// AWS.config.update({ region: "us-west-2"});

exports.handler = async (event, context) => {
//  const ddb = new AWS.DynamoDB({ apiVersion: "2012-10-08" });
 const documentClient = new AWS.DynamoDB.DocumentClient({ region: "us-west-2"}); 

 let responseBody = "";
 let statusCode = 0;

const {id, empresa, cnpj, fantasia, endereco, iniciodecontrato, vigenciadecontrato, modalidade, area, normas, objects} = JSON.parse(event.body);

 const params = {
	TableName: "Consultorias",
	Item: {
	    id: id,
      empresa: empresa,
      cnpj: cnpj,
      fantasia: fantasia,
      endereco: endereco,
      iniciodecontrato: iniciodecontrato,
      vigenciadecontrato: vigenciadecontrato,
      modalidade: modalidade,
      area: area,
      normas: normas,
      objects: objects
	    }
    };

      try {
        const data = await documentClient.put(params).promise();
        responseBody = JSON.stringify(data);
        statusCode = 201;
      } catch (err) {
        responseBody = `Unable to put consultorias: ${err}`;
        statusCode = 403;
      }

  const response = {
     statusCode: statusCode,
     headers: {
       "content-type": "application/json",
       "access-control-allow-origin": "*"
     },
     body: responseBody
  };

 return response;
};