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


elegible(Nombre) :-
    experiencia(Nombre, Exp),
    Exp >= 2,
    habilidad(Nombre, programacion),
    habilidad(Nombre, trabajo_en_equipo).
