import './styles/main.css';
import { startApp } from 'narrat';

window.addEventListener('load', () => {
  startApp({
    charactersPath: 'data/characters.json',
    configPath: 'data/config.json',
  }, {
    debug: true,
    logging: false,
  });
});

