child(prince, charles).
child(princess, ann).
child(prince, andrew).
child(prince, edward).

male(X) :- child(prince, X).
female(Y) :- child(princess, Y).

older(charles, ann).
older(ann, andrew).
older(andrew, edward).

is_older(A, B):- older(A, B).
is_older(A, B):- older(A, M), is_older(M, B).

then(A, B) :- child(prince, A), child(princess, B).
then(A, B) :- child(prince, A), child(prince, B), is_older(A, B).
then(A, B) :- child(princess, A), child(princess, B), is_older(A, B).

heirs(X, Y) :- insert_sort(X, Y).

insert_sort(X, Y) :- i_sort(X, [], Y).
i_sort([], Acc, Acc).
i_sort([H|T], Acc, Y) :- insert(H, Acc, NewAcc), i_sort(T, NewAcc, Y).

insert(X, [], [X]).
insert(X, [Y|T], [X, Y|T]) :- then(X, Y).
insert(X, [Y|T], [Y|NewT]) :- not(then(X, Y)), insert(X, T, NewT).

oldRoyalSuccession(OldRoyalSuccession):- findall(Y,child(_,Y), Offsprings), heirs(Offsprings,OldRoyalSuccession).
