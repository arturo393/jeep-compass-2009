#!/usr/bin/env node
import yargs from 'yargs';
import { hideBin } from 'yargs/helpers';
import axios from 'axios';
import dotenv from 'dotenv';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

// Load env
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
dotenv.config({ path: join(__dirname, '.env') });

const TRELLO_API_KEY = process.env.TRELLO_API_KEY;
const TRELLO_TOKEN = process.env.TRELLO_TOKEN;
const JEEP_CARD_ID = '66a991ad129db686561a3541';

if (!TRELLO_API_KEY || !TRELLO_TOKEN) {
    console.error('Error: TRELLO_API_KEY or TRELLO_TOKEN not found in .env');
    process.exit(1);
}

yargs(hideBin(process.argv))
    .command('status', 'Get the current status of the Jeep Compass card', () => { }, async (argv) => {
        try {
            const response = await axios.get(
                `https://api.trello.com/1/cards/${JEEP_CARD_ID}`,
                {
                    params: {
                        key: TRELLO_API_KEY,
                        token: TRELLO_TOKEN,
                    }
                }
            );

            const card = response.data;
            console.log('\n🚙  Jeep Compass Status');
            console.log('=======================');
            console.log(`Nombre: ${card.name}`);
            console.log(`Última Actividad: ${new Date(card.dateLastActivity).toLocaleString()}`);
            console.log(`URL: ${card.url}`);
            console.log('\n📋  Descripción Actual:');
            console.log('-----------------------');
            console.log(card.desc);
            console.log('-----------------------\n');

            const actionsResponse = await axios.get(
                `https://api.trello.com/1/cards/${JEEP_CARD_ID}/actions`,
                {
                    params: {
                        key: TRELLO_API_KEY,
                        token: TRELLO_TOKEN,
                        filter: 'commentCard',
                        limit: 5
                    }
                }
            );

            const comments = actionsResponse.data;
            if (comments.length > 0) {
                console.log('💬 Últimos Comentarios:');
                console.log('-----------------------');
                comments.forEach(comment => {
                    const date = new Date(comment.date).toLocaleString();
                    const text = comment.data.text;
                    const author = comment.memberCreator.fullName;
                    console.log(`[${date}] ${author}:`);
                    console.log(`${text}\n`);
                });
            } else {
                console.log('💬 No hay comentarios recientes.');
            }

        } catch (error) {
            console.error('Error fetching status:', error.response?.data || error.message);
        }
    })
    .demandCommand(1)
    .help()
    .argv;
