#!/usr/bin/python3

import jetson_inference
import jetson_utils
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str, help="filename of the image to process")
parser.add_argument("--network", type=str, default="resnet-18", help="model to use")
opt = parser.parse_args()
img = jetson_utils.loadImage(opt.filename)
net = jetson_inference.imageNet(
    opt.network,
    model="./resnet18.onnx",
    labels="./dataset/labels.txt",
    input_blob="input_0",
    output_blob="output_0"
)
class_idx, confidence = net.Classify(img)
class_desc = net.GetClassDesc(class_idx)
print("image is recognized as "+ str(class_desc) +" (class #"+ str(class_idx) +") with " + str(confidence*100)+"% confidence")
if str(class_desc)=="Benign":
    print("\nYou are not diagnosed with blood cancer.Here are some tips to prevent blood cancer."
          "\n1.gAvoid smokin"
          "\nSmoking increases the risk of some types of leukemia."
          "\nEven secondhand smoke has been linked to cancer risk."
          "\n2. Reduce Radiation Exposure"
          "\nHigh doses of ionizing radiation (like from nuclear accidents or frequent CT scans) can increase leukemia risk."
          "\nOnly undergo medical imaging when necessary."
          "\n3.Maintain a Healthy Immune System"
          "\nkeep your immune system strong with a balanced diet, Regular exercise, good sleep"
          "\nThere are still chances that you can get blood cancer in the future, so it's important to maintain a healthy lifestyle and go for regular checkups.")
if str(class_desc)=="[Malignant] Pre-B":
    print("\nYou are diagnosed with blood cancer ,Pre-B cell acute lymphoblastic leukemia(Pre-B ALL)."
          "\na type of blood cancer affecting immature B-cells—it's important to act quickly and thoughtfully. "
          "\n1.Confirm the Diagnosis"
          "\nGet a second opinion from a hematologist/oncologist, especially at a hospital with experience in leukemia."
          "\n2.Start Treatment Promptly"
          "\nPre-B ALL is aggressive but often treatable, especially if caught early. "
          "\nChemotherapy (first line of treatment)"
          "\nTargeted therapy (e.g., for Ph+ ALL, drugs like imatinib)"
          "\nStem cell transplant (in high-risk or relapsed cases)"
          "\nClinical trials (may offer cutting-edge treatments)"
          "\n3. Follow a Structured Treatment Plan"
          "\nTreatment often happens in phases:"
          "\nInduction therapy – to kill most leukemia cells"
          "\nConsolidation (intensification) – to kill remaining cancer"
          "\nMaintenance therapy – to prevent relapse (can last 2+ years)"
          "\n4.Take Care of Your Body and Mind"
          "\nEat well and rest—your body needs energy to recover."
          "\nStay hydrated and follow your doctor’s dietary advice."
          "\nAsk for mental health support—it’s normal to feel overwhelmed."
          "\nDo you want to know more about the Treatment?")
    answer=True
    while answer:
        questions=input("If you want,type the treatment you want to know among this list[Chemotherapy,Targeted therapy,Stem cell transplant,Clinical trials,Induction therapy,Consolidation (intensification),Maintenance therapy] ")
        if questions=="Chemotherapy":
            print("\nHere are explanation of Chemotherapy"
                  "\nWhat it is:"
                  "\nThe main treatment for Pre-B ALL. It uses drugs that kill fast-dividing cells, like cancer cells."
                  "\nHow it's given:"
                  "\nBy IV, pills, or spinal injection (intrathecal)"
                  "\nOften in cycles, allowing the body to rest between rounds"
                  "\nCommon drugs used:"
                  "\nVincristine, daunorubicin, cyclophosphamide, methotrexate, etc."
                  "\nSide effects:"
                  "\nHair loss, fatigue, infections, nausea, low blood counts—but many are temporary and manageable.")
            print("Do you want to know about other treatments to?")
            questions2=input("if you want to know press 1,if you do not want to press 2")
            if questions2=="1":
                print("ok!")
            else:
                answer=False
                print("Okay, no problem. Let me know if you want to learn more later!")
        if questions=="Targeted therapy":
            print("\nHere are explanation of Targeted Therapy"
                  "\nWhat it is:"
                  "\nUses drugs that target specific abnormal proteins or genes found in leukemia cells."
                  "\nWhen it's used:"
                  "\nEspecially for people with Philadelphia chromosome-positive ALL (Ph+ ALL)"
                  "\nDrugs block BCR-ABL, an abnormal fusion protein caused by that chromosome"
                  "\nCommon drugs:"
                  "\nImatinib (Gleevec)"
                  "\nDasatinib or Ponatinib"
                  "\nWhy it’s helpful:"
                  "\nIt directly interferes with leukemia growth without harming as many healthy cells.")
            print("Do you want to know about other treatments to?")
            questions2 = input("if you want to know press 1,if you do not want to press 2")
            if questions2 == "1":
                print("ok!")
            else:
                answer = False
                print("Okay, no problem. Let me know if you want to learn more later!")
        if questions=="Stem cell transplant":
            print("\nHere are the explanation of Stem Cell Transplant"
                  "\nWhat it is:"
                  "\nReplaces your damaged or destroyed bone marrow with healthy stem cells (from yourself or a donor)."
                  "\nWhen it’s used:"
                  "\nFor high-risk patients"
                  "\nIf the leukemia comes back after treatment (relapse)"
                  "\nSteps involved:"
                  "\nHigh-dose chemotherapy (to destroy diseased marrow)"
                  "\nInfusion of healthy stem cells (to rebuild the immune system)"
                  "\nRisks:"
                  "\nGraft-versus-host disease (if from donor), infections, long recovery")
            print("Do you want to know about other treatments to?")
            questions2 = input("if you want to know press 1,if you do not want to press 2")
            if questions2 == "1":
                print("ok!")
            else:
                answer = False
                print("Okay, no problem. Let me know if you want to learn more later!")
        if questions=="Clinical trials":
            print("\nHere are the explanations of Clinical Trials"
                  "\nWhat they are:"
                  "\nResearch studies that test new treatments or combinations that aren't yet widely available."
                  "\nWhy consider them:"
                  "\nAccess to cutting-edge treatments"
                  "\nMay be an option if standard treatments don’t work"
                  "\nAsk your doctor:"
                  "\nAre there trials available for your specific type of leukemia?"
                  "\nWhat are the risks/benefits?")
            print("Do you want to know about other treatments to?")
            questions2 = input("if you want to know press 1,if you do not want to press 2")
            if questions2 == "1":
                print("ok!")
            else:
                answer = False
                print("Okay, no problem. Let me know if you want to learn more later!")
        if questions=='Induction therapy':
            print("Here are the explanations of Induction therapy"
                  "\nGoal:"
                  "\nTo kill as many leukemia cells as possible and bring the disease into remission (meaning no signs of leukemia in bone marrow or blood"
                  "\nDuration:"
                  "\nUsually 4–6 weeks"
                  "\nWhat happens:"
                  "\nIntensive chemotherapy"
                  "\nClose monitoring in hospital (especially early on)"
                  "\nBlood and platelet transfusions if needed"
                  "\nSuccess rate:"
                  "\nMost patients reach remission after induction.")
            print("Do you want to know about other treatments to?")
            questions2 = input("if you want to know press 1,if you do not want to press 2")
            if questions2 == "1":
                print("ok!")
            else:
                answer = False
                print("Okay, no problem. Let me know if you want to learn more later!")
        if questions=="Maintenance therapy":
            print("\nHere are the explanations of Maintenance Therapy"
                  "\nGoal:"
                  "\nTo keep leukemia from coming back (long-term control)."
                  "\nTreatment:"
                  "\nLow-dose chemo over 1.5 to 2 years"
                  "\nOften includes oral medication at home (e.g., daily mercaptopurine)"
                  "\nWhy it matters:"
                  "\nEven if you feel well, maintenance is vital to prevent relapse.")
            questions2 = input("if you want to know press 1,if you do not want to press 2")
            if questions2 == "1":
                print("ok!")
            else:
                answer = False
                print("Okay, no problem. Let me know if you want to learn more later!")
if str(class_desc)=="[Malignant] early Pre-B":
    print("\nYou are diagnosed with early blood cancer, Pre-B cell acute lymphoblastic leukemia(Pre-B ALL)."
          "\na type of blood cancer affecting immature B-cells—it's important to act quickly and thoughtfully."
          "Early means it was caught before it spread too far—this is good for treatment success. "
          "\n1.Confirm the Diagnosis"
          "\nGet a second opinion from a hematologist/oncologist, especially at a hospital with experience in leukemia."
          "\n2.Start Treatment Promptly"
          "\nPre-B ALL is aggressive but often treatable, especially if caught early. "
          "\nChemotherapy (first line of treatment)"
          "\nTargeted therapy (e.g., for Ph+ ALL, drugs like imatinib)"
          "\nStem cell transplant (in high-risk or relapsed cases)"
          "\nClinical trials (may offer cutting-edge treatments)"
          "\n3. Follow a Structured Treatment Plan"
          "\nTreatment often happens in phases:"
          "\nInduction therapy – to kill most leukemia cells"
          "\nConsolidation (intensification) – to kill remaining cancer"
          "\nMaintenance therapy – to prevent relapse (can last 2+ years)"
          "\n4.Take Care of Your Body and Mind"
          "\nEat well and rest—your body needs energy to recover."
          "\nStay hydrated and follow your doctor’s dietary advice."
          "\nAsk for mental health support—it’s normal to feel overwhelmed."
          "\nDo you want to know more about the Treatment?")
    answer = True
    while answer:
        questions = input(
            "If you want,type the treatment you want to know among this list[Chemotherapy,Targeted therapy,Stem cell transplant,Clinical trials,Induction therapy,Consolidation (intensification),Maintenance therapy] ")
        if questions == "Chemotherapy":
            print("\nHere are explanation of Chemotherapy"
                  "\nWhat it is:"
                  "\nThe main treatment for Pre-B ALL. It uses drugs that kill fast-dividing cells, like cancer cells."
                  "\nHow it's given:"
                  "\nBy IV, pills, or spinal injection (intrathecal)"
                  "\nOften in cycles, allowing the body to rest between rounds"
                  "\nCommon drugs used:"
                  "\nVincristine, daunorubicin, cyclophosphamide, methotrexate, etc."
                  "\nSide effects:"
                  "\nHair loss, fatigue, infections, nausea, low blood counts—but many are temporary and manageable.")
            print("Do you want to know about other treatments to?")
            questions2 = input("if you want to know press 1,if you do not want to press 2")
            if questions2 == "1":
                print("ok!")
            else:
                answer = False
                print("Okay, no problem. Let me know if you want to learn more later!")
        if questions == "Targeted therapy":
            print("\nHere are explanation of Targeted Therapy"
                  "\nWhat it is:"
                  "\nUses drugs that target specific abnormal proteins or genes found in leukemia cells."
                  "\nWhen it's used:"
                  "\nEspecially for people with Philadelphia chromosome-positive ALL (Ph+ ALL)"
                  "\nDrugs block BCR-ABL, an abnormal fusion protein caused by that chromosome"
                  "\nCommon drugs:"
                  "\nImatinib (Gleevec)"
                  "\nDasatinib or Ponatinib"
                  "\nWhy it’s helpful:"
                  "\nIt directly interferes with leukemia growth without harming as many healthy cells.")
            print("Do you want to know about other treatments to?")
            questions2 = input("if you want to know press 1,if you do not want to press 2")
            if questions2 =="1" :
                print("ok!")
            else:
                answer = False
                print("Okay, no problem. Let me know if you want to learn more later!")
        if questions == "Stem cell transplant":
            print("\nHere are the explanation of Stem Cell Transplant"
                  "\nWhat it is:"
                  "\nReplaces your damaged or destroyed bone marrow with healthy stem cells (from yourself or a donor)."
                  "\nWhen it’s used:"
                  "\nFor high-risk patients"
                  "\nIf the leukemia comes back after treatment (relapse)"
                  "\nSteps involved:"
                  "\nHigh-dose chemotherapy (to destroy diseased marrow)"
                  "\nInfusion of healthy stem cells (to rebuild the immune system)"
                  "\nRisks:"
                  "\nGraft-versus-host disease (if from donor), infections, long recovery")
            print("Do you want to know about other treatments to?")
            questions2 = input("if you want to know press 1,if you do not want to press 2")
            if questions2 == "1":
                print("ok!")
            else:
                answer = False
                print("Okay, no problem. Let me know if you want to learn more later!")
        if questions == "Clinical trials":
            print("\nHere are the explanations of Clinical Trials"
                  "\nWhat they are:"
                  "\nResearch studies that test new treatments or combinations that aren't yet widely available."
                  "\nWhy consider them:"
                  "\nAccess to cutting-edge treatments"
                  "\nMay be an option if standard treatments don’t work"
                  "\nAsk your doctor:"
                  "\nAre there trials available for your specific type of leukemia?"
                  "\nWhat are the risks/benefits?")
            print("Do you want to know about other treatments to?")
            questions2 = input("if you want to know press 1,if you do not want to press 2")
            if questions2 == "1":
                print("ok!")
            else:
                answer = False
                print("Okay, no problem. Let me know if you want to learn more later!")
        if questions == 'Induction therapy':
            print("Here are the explanations of Induction therapy"
                  "\nGoal:"
                  "\nTo kill as many leukemia cells as possible and bring the disease into remission (meaning no signs of leukemia in bone marrow or blood"
                  "\nDuration:"
                  "\nUsually 4–6 weeks"
                  "\nWhat happens:"
                  "\nIntensive chemotherapy"
                  "\nClose monitoring in hospital (especially early on)"
                  "\nBlood and platelet transfusions if needed"
                  "\nSuccess rate:"
                  "\nMost patients reach remission after induction.")
            print("Do you want to know about other treatments to?")
            questions2 = input("if you want to know press 1,if you do not want to press 2")
            if questions2 == "1":
                print("ok!")
            else:
                answer = False
                print("Okay, no problem. Let me know if you want to learn more later!")
        if questions == "Maintenance therapy":
            print("\nHere are the explanations of Maintenance Therapy"
                  "\nGoal:"
                  "\nTo keep leukemia from coming back (long-term control)."
                  "\nTreatment:"
                  "\nLow-dose chemo over 1.5 to 2 years"
                  "\nOften includes oral medication at home (e.g., daily mercaptopurine)"
                  "\nWhy it matters:"
                  "\nEven if you feel well, maintenance is vital to prevent relapse.")
            questions2 = input("if you want to know press 1,if you do not want to press 2")
            if questions2 == "1":
                print("ok!")
            else:
                answer = False
                print("Okay, no problem. Let me know if you want to learn more later!")

if str(class_desc)=="[Malignant] Pro-B":
    print("You are diagnosed with blood cancer,malignant Pro-B cell acute lymphoblastic leukemia (Pro-B ALL) "
          "\n this generally means a more aggressive and high-risk form of leukemia."
          "\n1. Get Treated at a Specialized Cancer Center"
          "\nAsk for referral to a major hospital or leukemia center with expertise in aggressive leukemia."
          "\nEarly-stage but high-risk leukemias often need intensive treatment."
          "\n2.Begin Induction Chemotherapy Immediately"
          "\nThis phase kills most of the leukemia cells and puts you into remission."
          "\nIt usually involves strong multi-drug chemo over 4–6 weeks."
          "\nYou’ll be monitored closely—often in the hospital."
          "\n3.Genetic and Molecular Testing"
          "\nFind out exact mutations"
          "\nGuide targeted therapy (if available)"
          "\nDecide if you’re high risk"
          "\nFor example: rearrangements of KMT2A (MLL) are common in Pro-B ALL and often require more intensive therapy."
          "\n4.Supportive Care Is Crucial"
          "\nYou may experience:"
          "\nWeak immune system → avoid infections"
          "\nFatigue, nausea, low blood counts → get help managing symptoms"
          "\nYou’ll need:"
          "\nBlood transfusions"
          "\nPreventive antibiotics"
          "\nMental health support — this journey is tough, but you're not alone"
          "\nFinally Malignant Pro-B ALL is serious but treatable, especially when diagnosed early and treated intensively. "
          "\nFollow your medical team closely, and don’t hesitate to explore second opinions or new therapies.")




print("Ai is often wrong in its diagnosis.Please ask for more accurate examination at a hospital.")