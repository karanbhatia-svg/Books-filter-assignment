I completd asssignment using django rest framework. filter api url is (api/book_filters/) it can filter on the basis of title ,author_info ,language ,subjects,bookshelves ,mimetype, gutenberg_id .data will come in 20 records in descending popularity count.
for accessing remaining records i added paginator.we will page no in request too. here is example json:-
{
"author_info":null,
"title":null,
"subjects":null,
"language":"en",
"gutenberg_id":6,
"mimetype":null
"pageno":1
}
