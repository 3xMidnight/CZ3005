company(sumsum).
company(appy).
developed(sumsum,galacticaS3).
smartphonetech(galacticaS3).
stolen(stevey,galacticaS3,sumsum).
boss(stevey).
competitors(sumsum,appy).

rival(X) :- competitors(X,appy).
business(X) :- smartphonetech(X).
unethical(X) :- boss(X). business(Y), company(Z), rival(Z), stolen(X,Y,Z).
