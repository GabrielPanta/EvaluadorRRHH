% Generado autom�ticamente

experiencia(clara, 3).
habilidad(clara, programacion).
habilidad(clara, trabajo_en_equipo).
experiencia(gabriel, 2).
habilidad(gabriel, programacion).
habilidad(gabriel, trabajo_en_equipo).
experiencia(eduardo, 3).
habilidad(eduardo, programacion).
habilidad(eduardo, trabajo_en_equipo).
experiencia(ruth, 1).
habilidad(ruth, liderazgo).
experiencia(carlos, 2).
habilidad(carlos, liderazgo).
experiencia(gabriel_panta_jimenez, 5).
habilidad(gabriel_panta_jimenez, programacion).
habilidad(gabriel_panta_jimenez, trabajo_en_equipo).
experiencia(pedro_pascal, 1).
habilidad(pedro_pascal, liderazgo).
experiencia(marcos_gonzales, 3).
habilidad(marcos_gonzales, programacion).
habilidad(marcos_gonzales, trabajo_en_equipo).
experiencia(garcia_valdi_viezo_dalessandro, 7).
habilidad(garcia_valdi_viezo_dalessandro, programacion).
habilidad(garcia_valdi_viezo_dalessandro, trabajo_en_equipo).
experiencia(sofia_andrade, 5).
habilidad(sofia_andrade, programacion).
habilidad(sofia_andrade, trabajo_en_equipo).


elegible(Nombre) :-
    experiencia(Nombre, Exp),
    Exp >= 2,
    habilidad(Nombre, programacion),
    habilidad(Nombre, trabajo_en_equipo).
    
% Regla: Perfil técnico
perfil_tecnico(Nombre) :-
    habilidad(Nombre, programacion),
    experiencia(Nombre, Exp),
    Exp >= 2.

% Regla: Perfil liderazgo
perfil_liderazgo(Nombre) :-
    habilidad(Nombre, liderazgo),
    experiencia(Nombre, Exp),
    Exp >= 1.

% Regla: Nivel de experiencia
junior(Nombre) :- experiencia(Nombre, Exp), Exp < 2.
semisenior(Nombre) :- experiencia(Nombre, Exp), Exp >= 2, Exp < 4.
senior(Nombre) :- experiencia(Nombre, Exp), Exp >= 4.

% Regla: Perfil integral
perfil_integral(Nombre) :-
    habilidad(Nombre, programacion),
    habilidad(Nombre, trabajo_en_equipo),
    habilidad(Nombre, liderazgo),
    experiencia(Nombre, Exp),
    Exp >= 3.

% Regla: Sobresaliente
sobresaliente(Nombre) :-
    experiencia(Nombre, Exp),
    Exp >= 5,
    habilidad(Nombre, programacion),
    habilidad(Nombre, trabajo_en_equipo),
    habilidad(Nombre, liderazgo).

% Regla: Necesita formación
necesita_formacion(Nombre) :-
    \+ habilidad(Nombre, programacion).

