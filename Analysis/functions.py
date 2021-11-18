def test_knockout(model, gene_id):
    """Input 1: a SBML BiGG compliant GSMM.
    
    Input 2: ID of the gene of interest, as type 
    string or a list of several genes.
    """
    model = model
    print("---Before knockout---")
    print("Growth rate:", model.optimize().objective_value)
    copy_of_model1 = model.copy()
    with copy_of_model1:
        copy_of_model1.objective = copy_of_model1.reactions.rHb # Change in recombinant hemoglobin  
        copy_of_model1.optimize()
        print("Rate of hemoglobin production with hemoglobin as the objective: ", copy_of_model1.reactions.rHb.flux," [mmol / gDW / h]")
        print("Maximum theoretical yield of hemoglobin on glucose ", copy_of_model1.reactions.rHb.flux / (-1*copy_of_model1.reactions.EX_glc__D_e.flux),"[mmol-rHb / mmol-glucose]")
    
        
    copy_of_model2 = model.copy()
    with copy_of_model2 as test_mutant: 
        print("---After knockout---")
        
        if type(gene_id) is list: # If you want to knock-out multiple genes
            for i in range (0,len(gene_id)):
                gene = test_mutant.genes.get_by_id(gene_id[i]) # gene to knock out
                gene.knock_out() # knocks out the gene
        else: # if only one gene should be knocked-out
            gene = test_mutant.genes.get_by_id(gene_id) # gene to knock out
            gene.knock_out() # knocks out the gene
            print(test_mutant.genes.get_by_id(gene_id).name," knocked out.")
            
        test_mutant.objective = test_mutant.reactions.rHb # Change in recombinant hemoglobin
        test_mutant.optimize()
        print("Growth rate:", test_mutant.optimize().objective_value)#+" from the old growth rate, or a change of "+str(rate_change/old_rate*100)[:5]+"%.")     
        print("Rate of hemoglobin production:", test_mutant.reactions.EX_rHb.flux," [mmol / gDW / h]")
        print("Yield for hemoglobin on sugar", test_mutant.reactions.EX_rHb.flux / (-1*test_mutant.reactions.EX_glc__D_e.flux),"[mmol-rHb / mmol-glucose]")
        print("--------------------")
        #print("Before the knockout, the theoretical maximum yield of rHb on glucose [mmol-rHb / mmol-glucose] was: "+str(old_rhb_yield)[:9]+". Now the yield is: "+str(new_rhb_yield)[:9]+" which is a change of "+str(yield_change)+".") #+" and the rate is: "+str(new_rhb_production)[:6]


def add_rhb(model_input, model_output):
    """Function that adds a pseudoreaction for 
    a recombinant human haemoglobin protein (rHb).
    The function is a reaction that removes 
    all amino acids necessary for the contruction
    of a recombinant human haemoglobin protein, 
    and then adds +1*rHb.
    
    ------------Parameters------------
    model_input: path to the model as a BiGG
    compliant sbml file.
    model_output: name of the model with rHb.
    """
    from cobra import Reaction, Metabolite
    from cobra.io import write_sbml_model
    
    model = model_input # read_sbml_model(model_path) # loading of the model
    
    new_reaction_rHb = Reaction('rHb') # name of recombinant human haemoglobin protein
    hemoglobin = Metabolite(id='rHb_c', compartment='c') # adding recombinant human haemoglobin protein as a metabolite
    new_reaction_rHb.add_metabolites({model.metabolites.ala__L_c: -36*2,
                               model.metabolites.cys__L_c: -3*2,
                               model.metabolites.asp__L_c: -15*2,
                               model.metabolites.glu__L_c: -12*2,
                               model.metabolites.phe__L_c: -15*2,
                               model.metabolites.gly_c: -20*2,
                               model.metabolites.his__L_c: -19*2,
                               model.metabolites.lys__L_c: -22*2,
                               model.metabolites.leu__L_c: -36*2,
                               model.metabolites.met__L_c: -5*2,
                               model.metabolites.asn__L_c: -10*2,
                               model.metabolites.pro__L_c: -14*2,
                               model.metabolites.gln__L_c: -4*2,
                               model.metabolites.arg__L_c: -6*2,
                               model.metabolites.ser__L_c: -16*2,
                               model.metabolites.thr__L_c: -16*2,
                               model.metabolites.val__L_c: -31*2,
                               model.metabolites.trp__L_c: -3*2,
                               model.metabolites.tyr__L_c: -6*2, 
                               model.metabolites.pheme_m: -4,
                                  hemoglobin: 1,
                             })
    new_reaction_rHb.build_reaction_string()
    model.add_reactions([new_reaction_rHb])
    
    hemoglobin_exchange = Reaction('EX_rHb') # adding the exchange reaction for haemoglobin
    hemoglobin_exchange.add_metabolites({model.metabolites.rHb_c: -1})
    model.add_reaction(hemoglobin_exchange)
    
    medium = model.medium
    medium['EX_glc__D_e'] = 10
    model.medium = medium
    
    return write_sbml_model(model, model_output)


def get_rhb_pathway(model_path):
    """Function that returns a list of the enumerated
    pathway from glycine to heme.
    
    Parameters
    ----------
    model: SBML BiGG compliant model with the heme pathway
    
    The model must have a reaction from heme to haemoglobin,
    if it does not, run the add_rhb() function
    """
    from cobra.io import read_sbml_model, write_sbml_model
    from cobra import Reaction, Metabolite
    
    model = model_path # loading
    
    heme_1 = model.reactions.get_by_id('ALASm')
    heme_2 = model.reactions.get_by_id('PPBNGS')
    heme_3 = model.reactions.get_by_id('HMBS')
    heme_4 = model.reactions.get_by_id('UPP3S') 
    heme_12 = model.reactions.get_by_id('UPPDC1') 
    heme_13 = model.reactions.get_by_id('CPPPGO')
    heme_14 = model.reactions.get_by_id('PPPGOm')
    heme_15 = model.reactions.get_by_id('FCLTm')
    pseudo_rHb = model.reactions.get_by_id('rHb')
    
    rhb_pathway = [heme_1,heme_2,heme_3,heme_4,heme_12,heme_13,heme_14,heme_15, pseudo_rHb]
    return rhb_pathway


def read_yeast_model(model_path):
    """This function is a modified version of one that 
    was made by researchers at 
    Chalmers University of Technology Department of Biology
    and Biological Engineering Division of Systems and 
    Synthetic Biology in therir project titled 
    "The consensus GEM for Saccharomyces cerevisiae"
    which can be found at: https://github.com/SysBioChalmers/yeast-GEM
        
    The functions reads the SBML file of the yeast model using COBRA, 
    and imposes changes to the annotations so that the model is BiGG compliant.

    Parameters
    ----------
    make_bigg_compliant : bool, optional
        Whether the model should be initialized with BiGG compliance or not.
        If false, the original ids/names/compartments will be used instead.

    Returns
    -------
    cobra.core.Model
    """
    make_bigg_compliant=True
    
    import csv
    from cobra.io import read_sbml_model, write_sbml_model
    from copy import copy
    from dotenv import find_dotenv
    import os
    from os.path import dirname
    
    # Load model:
    MODEL_PATH = model_path
    model = read_sbml_model(MODEL_PATH)
    
    dotenv_path = find_dotenv()
    REPO_PATH = dirname(dotenv_path)

    # Check if already BiGG compliant:
    is_bigg_compliant = "x" in model.compartments

    # Convert to BiGG compliant if not already:
    if not is_bigg_compliant and make_bigg_compliant:
        # Load met/rxn dictionaries:
        def load_bigg_dict(bigg_file_path):
            bigg_dict = {}
            with open(bigg_file_path) as bigg_file:
                bigg_reader = csv.reader(bigg_file, delimiter=',')
                for row in bigg_reader:
                    bigg_dict[row[0]] = row[1]
            return bigg_dict
        data_path = f"{REPO_PATH}/data/databases"
        met_bigg_dict = load_bigg_dict(f"data/databases/BiGGmetDictionary_newIDs.csv")
        rxn_bigg_dict = load_bigg_dict(f"data/databases/BiGGrxnDictionary_newIDs.csv")

        # Function for adding unique ids to the model:
        def add_new_id(model_element, new_id):
            original_id = copy(new_id)
            id_assigned = False
            copy_number = 1
            while not id_assigned:
                try:
                    if hasattr(model_element, "compartment"):  # metabolites
                        model_element.id = f"{new_id}_{model_element.compartment}"
                    else:  # reactions
                        model_element.id = new_id
                    id_assigned = True
                except ValueError:
                    new_id = f"{original_id}_copy{str(copy_number)}"
                    copy_number += 1

        # Metabolite changes:
        comp_dic = {"er":"r", "erm":"rm", "p":"x"}
        for met in model.metabolites:
            # Save original id in notes:
            met.notes["Original ID"] = met.id
            # Change name to not include compartment at the end:
            met.name = met.name.replace(f" [{model.compartments[met.compartment]}]", "")
            # Change compartment info:
            if met.compartment in comp_dic:
                met.compartment = comp_dic[met.compartment]
            # Update id with BiGG information:
            if "bigg.metabolite" in met.annotation:
                add_new_id(met, met.annotation['bigg.metabolite'])
            elif met.id in met_bigg_dict:
                add_new_id(met, met_bigg_dict[met.id])
            else:
                met.id = met.id.replace(f"[{met.compartment}]", f"_{met.compartment}")

        # Compartment changes:
        comps = model.compartments
        comps["r"] = "endoplasmic reticulum"
        comps["rm"] = "endoplasmic reticulum membrane"
        comps["x"] = "peroxisome"
        model.compartments = comps

        # Reaction changes:
        for rxn in model.reactions:
            # Update id with BiGG information:
            if "bigg.reaction" in rxn.annotation:
                rxn.notes["Original ID"] = rxn.id
                add_new_id(rxn, rxn.annotation['bigg.reaction'])
            elif rxn.id in rxn_bigg_dict:
                rxn.notes["Original ID"] = rxn.id
                add_new_id(rxn, rxn_bigg_dict[rxn.id])

    return model


def write_yeast_model(model, model_output):
    from cobra.io import read_sbml_model, write_sbml_model
    """Writes the SBML file of the yeast model using COBRA.

    Parameters
    ----------
    model : cobra.core.Model
        Yeast model to be written
    model_output: name of the model
    """
    write_sbml_model(model, model_output)