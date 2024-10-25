import ROOT #Particle Physics Data Analysis Framework

def create_muon_vector(pt, eta, phi, mass):
    # Create a TLorentzVector and set its components
    muon_vector = ROOT.TLorentzVector()
    muon_vector.SetPtEtaPhiM(pt, eta, phi, mass)
    return muon_vector

def calculate_invariant_mass(pt1, eta1, phi1, mass1, pt2, eta2, phi2, mass2):
    # Create TLorentzVector objects for both muons
    muon1 = create_muon_vector(pt1, eta1, phi1, mass1)
    muon2 = create_muon_vector(pt2, eta2, phi2, mass2)

    # Add the two vectors
    combined_muon_vectors = muon1 + muon2

    # Calculate invariant mass
    invariant_mass = combined_muon_vectors.M()
    return invariant_mass


def process_input_file(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:

        # Create a ROOT histogram to store invariant masses
        hist = ROOT.TH1F("inv_mass", "Invariant Mass", 100, 0, 850)  # 100 bins between 0 and 850 GeV, to account for the amount of data
      
        while True:
            # Read the header line
            header = f_in.readline().strip()
            if not header:
                break  # End of file

            # Read and discard the second line (irrelevant data)
            f_in.readline()

            # Read the next two lines for muon data
            muon1_line = f_in.readline().strip()
            muon2_line = f_in.readline().strip()

            if muon1_line.startswith("m1") and muon2_line.startswith("m2"):
                    
                # Extract data for muon 1
                muon1_data = muon1_line.split()
                pt1 = float(muon1_data[2])
                eta1 = float(muon1_data[3])
                phi1 = float(muon1_data[4])
                mass1 = float(muon1_data[5])

                # Extract data for muon 2
                muon2_data = muon2_line.split()
                pt2 = float(muon2_data[2])
                eta2 = float(muon2_data[3])
                phi2 = float(muon2_data[4])
                mass2 = float(muon2_data[5])

                # Calculate invariant mass
                inv_mass = calculate_invariant_mass(pt1, eta1, phi1, mass1, pt2, eta2, phi2, mass2)
                f_out.write(f"Invariant Mass of {header}: {inv_mass} GeV\n")

                # Input the calculated invariant mass into the histogram
                hist.Fill(inv_mass)
                
                # Read the next header line
                f_in.readline()
                
            else:
                f_out.write(f"Invariant Mass of {header}: Missing or incorrect muon data\n")

    # Customize histogram appearance
    hist.SetTitle("Invariant Mass Distribution")
    hist.GetXaxis().SetTitle("Invariant Mass (GeV)")
    hist.GetYaxis().SetTitle("Number of Events")

    # Save histogram to PDF
    c1 = ROOT.TCanvas("c1", "Histogram Canvas", 800, 600)
    hist.Draw()
    c1.SaveAs("invariant_masses_histogram.pdf")

input_file = '/home/newHomeDir/Programming Projects/Project 1 - Invariant Mass/muons.txt'
output_file = '/home/newHomeDir/Programming Projects/Project 1 - Invariant Mass/invariant_masses.txt'
process_input_file(input_file, output_file)
