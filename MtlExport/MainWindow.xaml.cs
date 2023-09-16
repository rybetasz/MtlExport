using Microsoft.Win32;
using System;
using System.Collections.Generic;
using System.IO;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Controls.Primitives;
using System.Windows.Media;

namespace MtlExport
{
    public partial class MainWindow : Window
    {
        private string mtlFilePath = "";
        private string selectedGameString = "";

        public MainWindow()
        {
            InitializeComponent();

            SelectGame.Items.Add("UG1");
            SelectGame.Items.Add("UG2");
            SelectGame.Items.Add("NFSMW");
            SelectGame.Items.Add("NFSC");
            SelectGame.Items.Add("NFSPS");
            SelectGame.Items.Add("NFSUC");
            SelectGame.Items.Add("NFSW");
        }

        private void SelectFile_Click(object sender, RoutedEventArgs e)
        {
            OpenFileDialog openFileDialog1 = new OpenFileDialog();

            openFileDialog1.InitialDirectory = "c:\\";
            openFileDialog1.Filter = "Material Files (*.mtl, *.MTL)|*.mtl;*.MTL";
            openFileDialog1.FilterIndex = 2;
            openFileDialog1.RestoreDirectory = true;

            if (openFileDialog1.ShowDialog() == true)
            {
                mtlFilePath = openFileDialog1.FileName;
            }
        }

        private void Start_Click(object sender, RoutedEventArgs e)
        {
            if (string.IsNullOrEmpty(selectedGameString))
            {
                MessageBox.Show("Select the game first", "Error", MessageBoxButton.OK, MessageBoxImage.Error);
                UpdateStatusBar("Error");
                return;
            }

            SaveFileDialog saveFileDialog = new SaveFileDialog();
            saveFileDialog.Filter = "Text Files (*.txt)|*.txt";
            saveFileDialog.Title = "Export";
            if (saveFileDialog.ShowDialog() == true)
            {
                string outputFilePath = saveFileDialog.FileName;
                ExtractMaterials(mtlFilePath, outputFilePath, selectedGameString);
                UpdateStatusBar("Exported.  Output File:" + outputFilePath);
            }


        }

        private void SelectGame_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            ComboBox comboBox = (ComboBox)sender;
            string selectedGame = comboBox.SelectedItem as string;

            if (selectedGame == "UG1")
            {
                selectedGameString = "MATERIAL U";
            }
            else if (selectedGame == "UG2")
            {
                selectedGameString = "MATERIAL U2";
            }
            else if (selectedGame == "NFSMW")
            {
                selectedGameString = "MATERIAL MW";

            }
            else if (selectedGame == "NFSC")
            {
                selectedGameString = "MATERIAL C";
            }

            else if (selectedGame == "NFSPS")
            {
                selectedGameString = "MATERIAL PS";
            }

            else if (selectedGame == "NFSUC")
            {
                selectedGameString = "MATERIAL UC";
            }

            else if (selectedGame == "NFSW")
            {
                selectedGameString = "MATERIAL W";
            }
        }

        public static void ExtractMaterials(string mtlFilePath, string outputFilePath, string selectedGameString)
        {
            List<string> materials = new List<string>();

            using (StreamReader mtlFile = new StreamReader(mtlFilePath, System.Text.Encoding.UTF8))
            {
                string line;
                while ((line = mtlFile.ReadLine()) != null)
                {
                    line = line.Trim();
                    if (line.StartsWith("newmtl "))
                    {
                        string materialName = line.Substring("newmtl ".Length);
                        materials.Add($"{selectedGameString} {materialName}");
                    }
                }
            }

            File.WriteAllLines(outputFilePath, materials);


        }
        private void UpdateStatusBar(string message)
        {
            StatusText.Text = message;
        }
    }
}
