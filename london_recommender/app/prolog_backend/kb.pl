Ingrid Håbrekke, [4/14/2022 1:16 AM]
%  Tell prolog that known/3 and multivalued/1 will be added later
:- dynamic known/3 .

% Enter your KB below this line:

activity(hampstead_heath) :- vibe(active), \+has_bike(yes), \+willing_mask(yes).
activity(castle) :- vibe(active), \+has_bike(yes), willing_mask(yes).
activity(olympic_park) :- vibe(active), has_bike(yes).

activity(barb_lib) :- vibe(chill), need_to_work(yes), env(library).
activity(fidelio_cafe) :- vibe(chill), need_to_work(yes), \+env(library).
activity(st_pauls) :- vibe(chill), \+need_to_work(yes), walk(yes), travel_time(min).
activity(camden_market) :- vibe(chill), \+need_to_work(yes), walk(yes), travel_time(avg).
activity(richmond_park) :- vibe(chill), \+need_to_work(yes), walk(yes), travel_time(max).
activity(notting_hill) :- vibe(chill), \+need_to_work(yes), \+walk(yes), willing_mask(yes).
activity(leather_lane) :- vibe(chill), \+need_to_work(yes), \+walk(yes), \+willing_mask(yes).

activity(rooftop_bridge) :- vibe(energetic), vulnerable(yes).
activity(comedy_club) :- vibe(energetic), \+vulnerable(yes), energy(laughs).
activity(pub_crawl) :- vibe(energetic), \+vulnerable(yes), energy(alcohol).
activity(carwash) :- vibe(energetic), \+vulnerable(yes), energy(dance), travel_time(max).
activity(salsa_soho) :- vibe(energetic), \+vulnerable(yes), energy(dance), travel_time(avg).
activity(fabric) :- vibe(energetic), \+vulnerable(yes), energy(dance), travel_time(min).

activity(bun_house) :- vibe(food), meal(snack).
activity(circolo_popolare) :- vibe(food), meal(lunch).
activity(shake_shack) :- vibe(food), meal(dinner), budget(min).
activity(ngon_ngon) :- vibe(food), meal(dinner), budget(avg).
activity(moro) :- vibe(food), meal(dinner), budget(max).
activity(polo_bar) :- vibe(food), meal(breakfast), try_english(yes).
activity(dishoom) :- vibe(food), meal(breakfast), \+try_english(yes).
% The code below implements the prompting to ask the user:

vibe(X) :- ask_list(vibe, X).
has_bike(X) :- ask(has_bike, X).
need_to_work(X) :- ask(need_to_work, X).
vulnerable(X) :- ask(vulnerable, X).
meal(X) :- ask_list(meal, X).
willing_mask(X) :- ask(willing_mask,X).
env(X) :- ask(env, X).
walk(X) :- ask(walk,X).
energy(X) :- ask_list(energy, X).
budget(X) :- ask_list(budget,X).
try_english(X) :- ask(try_english, X).
travel_time(X) :- ask_list(travel_time,X).


% Asking clauses


% If not multivalued, and already known to be something else, don't ask again for a different value.

ask_list(A, V):-
known(yes, A, V),
!.

ask_list(A, V):-
known(yes, A, _),
!, fail.

ask_list(A, V):-
read_py(A, V, Y),
assertz(known(yes, A, Y)),
Y = V.

ask(A, V):-
known(yes, A, V), % succeed if true
!.  % stop looking

ask(A, V):-
known(_, A, V), % fail if false
!, fail.

ask(A, V):-
known(yes, A, V2),
V \== V2,
!, fail.

ask(A, V):-
read_py(A,V,Y), % get the answer
assertz(known(Y, A, V)), % remember it
Y == yes.  % succeed or fail