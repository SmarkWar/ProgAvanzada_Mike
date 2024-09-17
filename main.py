
"""
- Pacientes
- Medicos
- Habitaciones
- Consultas
- Medicamentos
    
"""

from paciente import Paciente
from hospital import Hospital
from medico import Medico

hospital = Hospital()

paciente= Paciente("Juan", 2004, 76, 1.78, "Avenida Madero")
paciente_dos= Paciente("Jonathan", 2005, 70, 1.90, "Circuito")

medico = Medico("Alberto", 1900, "COCM040323IJ7",  "Av. Periodismo")

hospital.registrar_paciente(paciente=paciente)
hospital.registrar_paciente(paciente=paciente_dos)

hospital.registrar_medico(medico=medico)

hospital.mostrar_pacientes()
    