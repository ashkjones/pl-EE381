import random, math

def generate(data):
   pa = random.randint(20,25)
   pb = 100 - pa
   pa_decimal = pa / 100.0
   pb_decimal = pb / 100.0

   pda = random.randint(3,6)
   pdb = random.randint(2,7)
   pda_decimal = pda / 100.0
   pdb_decimal = pdb /100.0

   pand = pda_decimal * pa_decimal
   pbnd = pdb_decimal * pb_decimal

   pd = pand + pbnd

   pad = pand / pd

   data["params"]["pa"] = pa
   data["params"]["pb"] = pb
   data["params"]["pa_decimal"] = round(pa_decimal, 4)
   data["params"]["pb_decimal"] = round(pb_decimal, 4)
   data["correct_answers"]["pb_decimal"] = round(pb_decimal, 4)
   data["params"]["pda"] = pda
   data["params"]["pdb"] = pdb
   data["params"]["pda_decimal"] = round(pda_decimal, 4)
   data["params"]["pdb_decimal"] = round(pdb_decimal, 4)
   data["params"]["pand"] = round(pand, 4)
   data["correct_answers"]["pbnd"] = round(pbnd, 4)
   data["correct_answers"]["pd"] = round(pd, 4)
   data["correct_answers"]["pad"] = round(pad, 4)

