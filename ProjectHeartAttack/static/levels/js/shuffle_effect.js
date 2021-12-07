
 let b = baffle('.text_description', {
   characters: '+-\u2022~\u2591\u2588\u2593 \u2593\u2592\u2591!=*',
   speed: 75
 });
 b.start();
 b.reveal(2000);

 let text_author = baffle('.author_by', {
    characters: '+-\u2022~\u2591\u2588\u2593 \u2593\u2592\u2591!=*',
    speed: 75
 });
 text_author.start();
 text_author.reveal(1000);

 let text_diffculty = baffle('.name_level_page', {
    characters: '+-\u2022~\u2591\u2588\u2593 \u2593\u2592\u2591!=*',
    speed: 75
 });
 text_diffculty.start();
 text_diffculty.reveal(1000);

 let text_rating = baffle('.rating_num', {
    characters: '+-\u2022~\u2591\u2588\u2593 \u2593\u2592\u2591!=*',
    speed: 90
 });
 text_rating.start();
 text_rating.reveal(1000);

 let author_level = baffle('.title_by_level', {
    characters: '+-\u2022~\u2591\u2588\u2593 \u2593\u2592\u2591!=*',
    speed: 75
 });
 author_level.start();
 author_level.reveal(1000);