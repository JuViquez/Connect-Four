class ConnectFourScore:

    def search_spaces(self, combinations, value):
        max_score = 0
        for cb in combinations:
            cb = cb.tolist()
            space_r = -1
            space_l = -1
            disc_index = cb.index("C")
            if disc_index < 3 and cb[disc_index + 1] is None:
                space_r += 1 
                for i in range(disc_index + 1, 4):
                    if cb[i] == value:
                        space_r += 1
                    elif cb[i] is not None:
                        space_r = -1
                        break
            if disc_index > 0 and cb[disc_index - 1] is None:
                space_l += 1 
                for i in reversed(range(0,disc_index - 1)):
                    if cb[i] == value:
                        space_l += 1
                    elif cb[i] is not None:
                        space_l = -1
                        break
            if space_l > 0 or space_r > 0:
                current_score = cb.count(value)
                max_score += current_score

        return max_score
    
    def score_sequence(self, combinations, value):
        score = 0
        for cb in combinations:
            cb_score = 0
            cb_len = len(cb)
            for i in range(cb_len):
                if cb[i] == value:
                    cb_score += 1
                elif cb[i] == "C":
                    if i == 0:
                        if cb[i+1] != value:
                            cb_score = 0
                            break
                    elif i == cb_len-1:
                        if cb[i-1] != value:
                            cb_score = 0
                            break
                    elif cb[i+1] != value and cb[i-1] != value:
                        cb_score = 0
                        break
                elif cb[i] != None:
                    cb_score = 0
                    break
            score += cb_score
        return score
    
    def score_combinations(self, combinations, value):
        score = 0
        for cb in combinations:
            cb_score = 0
            for slot in cb:
                print(slot)
                if slot == value:
                    cb_score += 1
                elif slot != None:
                    cb_score = 0
                    break
            score += cb_score
        return score
