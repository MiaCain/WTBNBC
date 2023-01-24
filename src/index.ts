import 'narrat/dist/style.css';
import './styles/main.css';
import { startApp } from 'narrat';

window.addEventListener('load', () => {
  startApp({
    charactersPath: 'data/characters.yaml',
    configPath: 'data/config.yaml',
  });
});

