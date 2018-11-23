class ConnectFourScore:

    def search_spaces(self, board, combinations, value):
        max_score = 0
        subvalue = "r"
        if value == "Y":
            subvalue = "y"
        #print("Numpy list")
        for cb in combinations:
            cb = cb.tolist()
            #print(cb)
            space_r = -1
            space_l = -1
            disc_index = cb.index(subvalue)
            #print("index " + str(disc_index))
            #disc_index = np.where(cb == subvalue)
            if disc_index < 3 and cb[disc_index + 1] is None:
                space_r += 1 
                for i in range(disc_index + 1, 4):
                    if cb[i] == value:
                        space_r += 1
                    elif cb[i] is not None:
                        break
            if disc_index > 0 and cb[disc_index - 1] is None:
                space_l += 1 
                for i in reversed(range(0,disc_index - 1)):
                    if cb[i] == value:
                        space_l += 1
                    elif cb[i] is not None:
                        break
            if space_l > 0 or space_r > 0:
                current_score = cb.count(value)
                if current_score == 2:
                    max_score = 2
                    break
                elif current_score > max_score:
                    max_score = current_score
                """
                print(cb.count(value))
                print(space_r)
                print(space_l)
                """
        return max_score