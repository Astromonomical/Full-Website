function deleteQuote(quoteId) {
    fetch('/delete-quote', {
        method: 'POST',
        body: JSON.stringify({ quoteId: quoteId})
    }).then((_res) => {
        window.location.href = "/createquote";
    });
}
