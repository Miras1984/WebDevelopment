let ask = (question, yes, no) => confirm(question) ? yes() : no();
ask(
    'Do you agree?',
    () => console.log('You agreed'),
    () => console.log('You interrupted execution'),
);