# -*- coding: utf-8 -*-



############## Ionic Fluorination without destabilization via Ca2+ ##################

# pairing a carbocation with fluoride
# simulates the step-by-step defluorination described in the enzyme concept (removal of F, adding hydride)
# done for propanoic acid all the way to 3,3,3,2,2-pentafluoropropanoic acid, to simulate all major occuring C-F bond circumstances

"""
R1: [CH₂CH₂COOH]+ + F- --> CFH₂CH₂COOH
R2: [CFHCH₂COOH]+ + F- --> CF₂HCH₂COOH
R3: [CF₂CH₂COOH]+ + F- --> CF₃CH₂COOH
R4: [CF₃CHCOOH]+ + F- --> CF₃CFHCOOH
R5: [CF₃CFCOOH]+ + F- --> CF₃CF₂COOH
"""
G_propanoic_acid = -268.15679997
G_3_fluoropropanoic_acid = -367.35767305
G_3_3_difluoropropanoic_acid = -466.57409010
G_3_3_3_trifluoropropanoic_acid = -565.79283971
G_3_3_3_2_tetrafluoropropanoic_acid = -664.98187540
G_3_3_3_2_2_pentafluoropropanoic_acid = -764.18167951

G_3_fluoropropanoic_acid_defluorinated = -267.30848820
G_3_3_difluoropropanoic_acid_defluorinated = -366.52266234
G_3_3_3_trifluoropropanoic_acid_defluorinated = -465.73788201
G_3_3_3_2_tetrafluoropropanoic_acid_defluorinated = -564.91661763
G_3_3_3_2_2_pentafluoropropanoic_acid_defluorinated = -664.10797447
G_fluoride = -99.93509945

dGr_R1_ionic = round(
    G_3_fluoropropanoic_acid - (G_3_fluoropropanoic_acid_defluorinated + G_fluoride), 3
    ) * 2625.5

dGr_R2_ionic = round(
    G_3_3_difluoropropanoic_acid - (G_3_3_difluoropropanoic_acid_defluorinated + G_fluoride), 3
    ) * 2625.5

dGr_R3_ionic = round(
    G_3_3_3_trifluoropropanoic_acid - (G_3_3_3_trifluoropropanoic_acid_defluorinated + G_fluoride), 3
    ) * 2625.5

dGr_R4_ionic = round(
    G_3_3_3_2_tetrafluoropropanoic_acid - (G_3_3_3_2_tetrafluoropropanoic_acid_defluorinated + G_fluoride), 3
    ) * 2625.5

dGr_R5_ionic = round(
    G_3_3_3_2_2_pentafluoropropanoic_acid - (G_3_3_3_2_2_pentafluoropropanoic_acid_defluorinated + G_fluoride), 3
    ) * 2625.5


print(dGr_R1_ionic)
print(dGr_R2_ionic)
print(dGr_R3_ionic)
print(dGr_R4_ionic)
print(dGr_R5_ionic)

#%%
"""
These are great results because P680* provides far more energy with photons than those values
However, there is another challenge: The redox potential...

dG = -n * F * E
E = dG/(-n * F)

n = number of electrons, F = Faraday constant, E = redox potential
F = 96.5 kJ/mol

"""

needed_redox_potential_R1 = round(dGr_R1_ionic/(-1 * 96.5), 3)
needed_redox_potential_R2 = round(dGr_R2_ionic/(-1 * 96.5), 3)
needed_redox_potential_R3 = round(dGr_R3_ionic/(-1 * 96.5), 3)
needed_redox_potential_R4 = round(dGr_R4_ionic/(-1 * 96.5), 3)
needed_redox_potential_R5 = round(dGr_R5_ionic/(-1 * 96.5), 3)

print(needed_redox_potential_R1)
print(needed_redox_potential_R2)
print(needed_redox_potential_R3)
print(needed_redox_potential_R4)
print(needed_redox_potential_R5)

"""
These redox-potentials cannot be overcome by pure oxidation... P680*+ has a redox potential of +1.25 V
Idea: Bring Ca2+ extremely close to fluorine, thus destabilizing the bond. The necessary redox potential will be far
smaller.
"""

#%%############# Ionic Fluorination with destabilization via Ca2+ ##################
    

















