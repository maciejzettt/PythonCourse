def get_n_colors(col_list, n):
    ret = col_list[:n]
    return ret


colors = ["red", "orange", "green", "violet", "blue", "yellow"]

text = "Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką " \
       "prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji " \
       "zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w " \
       "imię postępu. Rządzi w niej prawo dżungli. "

definition = text[text.find('(')+1:text.find(')')]
print(definition)