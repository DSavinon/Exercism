class lasagna:

    # TODO: define the 'EXPECTED_BAKE_TIME' constant
    def EXPECTED_BAKE_TIME():
        time = 40
        return time

    # TODO: consider defining the 'PREPARATION_TIME' constant
    #       equal to the time it takes to prepare a single layer

    # TODO: define the 'bake_time_remaining()' function
    def bake_time_remaining(elapsed_bake_time: int):
        """Calculate the bake time remaining.

        :param elapsed_bake_time: int - baking time already elapsed.
        :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

        Function that takes the actual minutes the lasagna has been in the oven as
        an argument and returns how many minutes the lasagna still needs to bake
        based on the `EXPECTED_BAKE_TIME`.
        """
        time_left = lasagna.EXPECTED_BAKE_TIME() - elapsed_bake_time
        return time_left
        pass

    # TODO: define the 'preparation_time_in_minutes()' function
    #       and consider using 'PREPARATION_TIME' here
    def prepration_time_in_minutes(layers: int):
        """Calculamos el tiempo que nos toma preparar la lasagna, dependiendo de cada capa
        :param layers: int
        :return: int - 2 minutos por cada capa
        """
        prep_tiempo = layers * 2
        return prep_tiempo

    # TODO: define the 'elapsed_time_in_minutes()' function
    def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
        """Calculamos el total de minutos que hemos estado cocinando
        :param number_of_layers: int
        :param elapsed_bake_time: int
        :return: int - minutos que se ha estado cocinando
        """
        total_minutes = (
            lasagna.prepration_time_in_minutes(number_of_layers) + elapsed_bake_time
        )
        return total_minutes


print(lasagna.elapsed_time_in_minutes(3, 20))
