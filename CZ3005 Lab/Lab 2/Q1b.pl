company(sumsum).
company(appy).
boss(stevey).
smartphonetech(galacticaS3).
competitors(sumsum,appy).
developed(sumsum,galacticaS3).
stolen(stevey,galacticaS3,sumsum).

rival(X) :- competitors(X,appy).
business(X) :- smartphonetech(X).
unethical(X) :- boss(X). business(Y), company(Z), rival(Z), stolen(X,Y,Z).
