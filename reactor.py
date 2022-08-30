class Reactor:
    
    def is_criticality_balanced(temperature: float, neutrons_emitted: float) -> bool:
        """Calculamos si el reactor esta criticamente balanceado

        Args:
            temperature (float): [Temperatura del reactor, debe de estar por debajo de los 800 grados K]
            neutrons_emitted (float): [Neutrones emitidos por segundo deben ser mayor a 500]

        Returns:
            bool: [True si temp mayor a 800, nuetrons mayor a 500 y si su multiplicacion es menor a 500,000; False de lo contratio]
        """
        if temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000:
            return True
        else:
            return False

    def reactor_efficiency(voltage: float, current: float, theoretical_max_power: float) -> str:
        """Calculamos la funcion del reactor 

        Args:
            voltage (float)
            current (float)
            theoretical_max_power (float): [poder que corresponde al 100% de eficiencia]

        Returns:
            str: [Green con 80% o mas; Orange entre 80% y 60%; Red entre 60% y 30%; Red menor al 30%]
        """
        generated_power = voltage * current
        eficiencia = (generated_power/theoretical_max_power) * 100

        if eficiencia >= 80:
            return "green"
        elif eficiencia < 80 and eficiencia >= 60:
            return "orange"
        elif eficiencia < 60 and eficiencia >= 30:
            return "red"
        else:
            return "black" 

    def fail_safe(temperature: float, neutrons_produced_per_second: float, threshold: float) -> str:
        """Nos dice el estado del reactor dependiendo del porcentaje con relacion al Threshold

        Args:
            temperature ([float])
            neutrons_produced_per_second ([float])
            threshold ([float])

        Returns:
        str: [Low si esta debajo del 90%; Normal si esta +/- 10% del 100%; Danger si esta fuera de los otros rangos]
        """
        new_product =  temperature * neutrons_produced_per_second
        new_porcentaje = (new_product * 100) / threshold

        if new_porcentaje < 90:
            return "LOW"
        elif new_porcentaje > 90 and new_porcentaje < 110:
            return "NORMAL"

        return "DANGER"

    print(fail_safe(temperature=1000, neutrons_produced_per_second=30, threshold=5000))