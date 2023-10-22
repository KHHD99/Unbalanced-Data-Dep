import streamlit as st
import pandas as pd
import numpy as np
import pickle

path_models='https://drive.google.com/drive/folders/1BKnTr6dmAf8DFDbwesoyRfIEQeAKHgfY?usp=share_link'

def header():
    col1, col2  = st.columns([3, 1])
    with col1:
        st.markdown("""<h3 style='color: orange;'>HADDOU Khalid</h3>""", unsafe_allow_html=True)
    with col2:
        st.markdown("<h3 style='color: green;'>GrassFields</h3>", unsafe_allow_html=True)
        st.image('GF_logo/GRASSFIELDS_LogoBG.png', width=150)

# Create a function for the Test page
def Test():
 
    def display_user_input_parameters_CC():  
        # Collects user input features into dataframe
        st.sidebar.header('User Input Parameters')
        st.sidebar.markdown("""
        [Example of CC input file](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
        """)
        uploaded_file = st.sidebar.file_uploader("Upload your input CSV file for CC", type=["csv"])
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
        else:
            def user_input_features():
                Time= st.sidebar.slider('Time', 0, 172792, 1 )
                V1 = st.sidebar.slider('V 1', -56, 2, 1 )
                V2 = st.sidebar.slider('V 2', -72, 22, 1 )
                V3 = st.sidebar.slider('V 3', -48, 9, 1 )
                V4 = st.sidebar.slider('V 4', -5, 16, 1 )
                V5 = st.sidebar.slider('V 5', -113, 34, 1 )
                V6 = st.sidebar.slider('V 6', -26, 73, 1 )
                V7 = st.sidebar.slider('V 7', -43, 120, 1 )
                V8 = st.sidebar.slider('V 8', -73, 20, 1 )
                V9 = st.sidebar.slider('V 9', -13, 15, 1 )
                V10 = st.sidebar.slider('V 10', -24, 23, 1 )
                V11 = st.sidebar.slider('V 11', -4, 12, 1 )
                V12 = st.sidebar.slider('V 12', -18, 7, 1 )
                V13 = st.sidebar.slider('V 13', -5, 7, 1 )
                V14 = st.sidebar.slider('V 14', -19, 10, 1 )
                V15 = st.sidebar.slider('V 15', -4, 8, 1 )
                V16 = st.sidebar.slider('V 16', -14, 17, 1 )
                V17 = st.sidebar.slider('V 17', -25, 9, 1 )
                V18 = st.sidebar.slider('V 18', -9, 5, 1 )
                V19 = st.sidebar.slider('V 19', -7, 5, 1 )
                V20 = st.sidebar.slider('V 20', -54, 39, 1 )
                V21 = st.sidebar.slider('V 21', -34, 27, 1 )
                V22 = st.sidebar.slider('V 22', -10, 10, 1 )
                V23 = st.sidebar.slider('V 23', -44, 22, 1 )
                V24 = st.sidebar.slider('V 24', -2, 4, 1 )
                V25 = st.sidebar.slider('V 25', -10, 7, 1 )
                V26 = st.sidebar.slider('V 26', -2, 3, 1 )
                V27 = st.sidebar.slider('V 27', -22, 31, 1 )
                V28 = st.sidebar.slider('V 28', -15, 33, 1 )
                Amount = st.sidebar.slider('Amount', 0, 25691, 1 )
                data = {'Time':Time, 'V1':V1, 'V2':V2, 'V3':V3, 'V4':V4, 'V5':V5, 'V6':V6, 'V7':V7, 'V8':V8, 'V9':V9, 
                        'V10':V10, 'V11':V11, 'V12':V12, 'V13':V13, 'V14':V14, 'V15':V15, 'V16':V16, 'V17':V17, 'V18':V18, 'V19':V19,
                        'V20':V20, 'V21':V21, 'V22':V22, 'V23':V23, 'V24':V24, 'V25':V25, 'V26':V26, 'V27':V27, 'V28':V28, 'Amount': Amount
                        }
                features = pd.DataFrame(data, index=[0])
                return features
            df = user_input_features()
        return df,uploaded_file

        # st.subheader('User Input parameters')
    
    def display_user_input_parameters_CMIYC():
        # Collects user input features into dataframe
        st.sidebar.header('User Input Parameters')
        st.sidebar.markdown("""
        [Example of CMIYC input file](https://www.kaggle.com/competitions/catch-me-if-you-can-intruder-detection-through-webpage-session-tracking2/data)
        """)
        uploaded_file = st.sidebar.file_uploader("Upload your input CSV file for CMIYC", type=["csv"])
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
        else:
            def user_input_features():
                session_id= st.sidebar.slider('session_id', 0, 253561, 10000 )
                site1 = st.sidebar.slider('site1', 1, 41601, 20000 )
                site10 = st.sidebar.slider('site10', 1, 5924, 3000 )
                site2 = st.sidebar.slider('site2', 1, 41599, 30000 )
                site3 = st.sidebar.slider('site3', 1, 41600, 20000 )
                site4 = st.sidebar.slider('site4', 1, 41599, 30000 )
                site5 = st.sidebar.slider('site5', 1, 41599, 30000 )
                site6 = st.sidebar.slider('site6', 1, 41599, 30000 )
                site7 = st.sidebar.slider('site7', 1, 41600, 20000 )
                site8 = st.sidebar.slider('site8', 1, 41600, 20000 )
                site9 = st.sidebar.slider('site9', 1, 41600, 20000 )
                data = {'session_id':session_id,
                        'site1':site1, 'site10':site10, 'site2':site2, 'site3':site3, 'site4':site4, 'site5':site5, 
                        'site6':site6, 'site7':site7, 'site8':site8, 'site9':site9 }
                features = pd.DataFrame(data, index=[0])
                return features
            df = user_input_features()
        return df,uploaded_file

        # st.subheader('User Input parameters')
    
    def display_user_input_parameters_IEEE():  
        # Collects user input features into dataframe
        st.sidebar.header('User Input Parameters')
        st.sidebar.markdown("""
        [Example of IEEE input file](https://www.kaggle.com/competitions/ieee-fraud-detection/data)
        """)
        uploaded_file = st.sidebar.file_uploader("Upload your input CSV file for IEEE", type=["csv"])
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
        else:
            # st.sidebar.write("Please upload a CSV file.")
            df = None
        return df, uploaded_file
    
    def display_user_input_parameters_LOAN():  
        # Collects user input features into dataframe
        st.sidebar.header('User Input Parameters')
        st.sidebar.markdown("""
        [Example of LOAN input file](https://www.kaggle.com/avikpaul4u/vehicle-loan-default-prediction)
        """)
        uploaded_file = st.sidebar.file_uploader("Upload your input CSV file for LOAN", type=["csv"])
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
        else:
            def user_input_features():
                unique_id = st.sidebar.slider('UNIQUEID', 417428 , 671084 , 126828)
                disbursed_amount = st.sidebar.slider('DISBURSED_AMOUNT', 13320 , 987354 , 487017 )
                asset_cost = st.sidebar.slider('ASSET_COST', 37000 , 1328954 , 645977 )
                ltv = st.sidebar.slider('LTV', 13 , 95 , 40 )
                branch_id = st.sidebar.slider('BRANCH_ID', 1 , 261 , 130 )
                supplier_id = st.sidebar.slider('SUPPLIER_ID', 10524 , 24803 , 7139 )
                manufacturer_id = st.sidebar.slider('MANUFACTURER_ID', 45 , 156 , 55 )
                current_pincode_id = st.sidebar.slider('CURRENT_PINCODE_ID',1 , 7345 , 3672 )
                date_of_birth = st.sidebar.slider('DATE_OF_BIRTH', 0 , 14416 , 7208 )
                employment_type = st.sidebar.slider('EMPLOYMENT_TYPE', 0 , 1 , 0 )
                disbursal_date = st.sidebar.slider('DISBURSAL_DATE', 0 , 83 , 41 )
                state_id = st.sidebar.slider('STATE_ID', 1 , 22 , 10 )
                employee_code_id = st.sidebar.slider('EMPLOYEE_CODE_ID', 1 , 3795 , 1897 )
                mobile_no_avl_flag = st.sidebar.slider('MOBILENO_AVL_FLAG', 1 , 1 , 0 )
                aadhar_flag = st.sidebar.slider('AADHAR_FLAG',0 , 1 , 0 )
                pan_flag = st.sidebar.slider('PAN_FLAG', 0 , 1 , 0 )
                voter_id_flag = st.sidebar.slider('VOTERID_FLAG', 0 , 1 , 0 )
                driving_flag = st.sidebar.slider('DRIVING_FLAG', 0 , 1 , 0 )
                passport_flag = st.sidebar.slider('PASSPORT_FLAG', 0 , 1 , 0 )
                perform_cns_score = st.sidebar.slider('PERFORM_CNS_SCORE', 0 , 890 , 445 )
                perform_cns_score_description = st.sidebar.slider('PERFORM_CNS_SCORE_DESCRIPTION', 0 , 19 , 9 )
                pri_no_of_accts = st.sidebar.slider('PRI_NO_OF_ACCTS', 0 , 453 , 226 )
                pri_active_accts = st.sidebar.slider('PRI_ACTIVE_ACCTS', 0 , 144 , 72 )
                pri_overdue_accts = st.sidebar.slider('PRI_OVERDUE_ACCTS',0 , 25 , 12 )
                pri_current_balance = st.sidebar.slider('PRI_CURRENT_BALANCE', -6678296 , 96524920 , 51601608 )
                pri_sanctioned_amount = st.sidebar.slider('PRI_SANCTIONED_AMOUNT', 0 , 1000000000 , 500000000 )
                pri_disbursed_amount = st.sidebar.slider('PRI_DISBURSED_AMOUNT', 0 , 1000000000 , 500000000 )
                sec_no_of_accts = st.sidebar.slider('SEC_NO_OF_ACCTS', 0 , 52 , 26 )
                sec_active_accts = st.sidebar.slider('SEC_ACTIVE_ACCTS', 0 , 36 , 18 )
                sec_overdue_accts = st.sidebar.slider('SEC_OVERDUE_ACCTS',0 , 8 , 4 )
                sec_current_balance = st.sidebar.slider('SEC_CURRENT_BALANCE', -574647 , 36032852 , 18303749 )
                sec_sanctioned_amount = st.sidebar.slider('SEC_SANCTIONED_AMOUNT',0 , 30000000 , 15000000 )
                sec_disbursed_amount = st.sidebar.slider('SEC_DISBURSED_AMOUNT',0 , 30000000 , 15000000 )
                primary_instal_amt = st.sidebar.slider('PRIMARY_INSTAL_AMT',0 , 25642806 , 12821403 )
                sec_instal_amt = st.sidebar.slider('SEC_INSTAL_AMT',0 , 4170901 , 2085450 )
                new_accts_in_last_six_months = st.sidebar.slider('NEW_ACCTS_IN_LAST_SIX_MONTHS', 0 , 35 , 17)
                delinquent_accts_in_last_six_months = st.sidebar.slider('DELINQUENT_ACCTS_IN_LAST_SIX_MONTHS', 0 , 20 , 10 )
                average_acct_age = st.sidebar.slider('AVERAGE_ACCT_AGE',0 , 191 , 95 )
                credit_history_length = st.sidebar.slider('CREDIT_HISTORY_LENGTH', 0 , 290 , 145 )
                no_of_inquiries = st.sidebar.slider('NO_OF_INQUIRIES', 0 , 36 , 18 )

                # Create a dictionary to store the values
                data = {
                    'UNIQUEID': unique_id, 'DISBURSED_AMOUNT': disbursed_amount, 'ASSET_COST': asset_cost, 'LTV': ltv, 'BRANCH_ID': branch_id,
                    'SUPPLIER_ID': supplier_id, 'MANUFACTURER_ID': manufacturer_id, 'CURRENT_PINCODE_ID': current_pincode_id,
                    'DATE_OF_BIRTH': date_of_birth, 'EMPLOYMENT_TYPE': employment_type, 'DISBURSAL_DATE': disbursal_date, 'STATE_ID': state_id,
                    'EMPLOYEE_CODE_ID': employee_code_id, 'MOBILENO_AVL_FLAG': mobile_no_avl_flag, 'AADHAR_FLAG': aadhar_flag,
                    'PAN_FLAG': pan_flag, 'VOTERID_FLAG': voter_id_flag, 'DRIVING_FLAG': driving_flag, 'PASSPORT_FLAG': passport_flag,
                    'PERFORM_CNS_SCORE': perform_cns_score, 'PERFORM_CNS_SCORE_DESCRIPTION': perform_cns_score_description,
                    'PRI_NO_OF_ACCTS': pri_no_of_accts, 'PRI_ACTIVE_ACCTS': pri_active_accts, 'PRI_OVERDUE_ACCTS': pri_overdue_accts,
                    'PRI_CURRENT_BALANCE': pri_current_balance, 'PRI_SANCTIONED_AMOUNT': pri_sanctioned_amount,
                    'PRI_DISBURSED_AMOUNT': pri_disbursed_amount, 'SEC_NO_OF_ACCTS': sec_no_of_accts, 'SEC_ACTIVE_ACCTS': sec_active_accts,
                    'SEC_OVERDUE_ACCTS': sec_overdue_accts, 'SEC_CURRENT_BALANCE': sec_current_balance,
                    'SEC_SANCTIONED_AMOUNT': sec_sanctioned_amount, 'SEC_DISBURSED_AMOUNT': sec_disbursed_amount,
                    'PRIMARY_INSTAL_AMT': primary_instal_amt, 'SEC_INSTAL_AMT': sec_instal_amt,
                    'NEW_ACCTS_IN_LAST_SIX_MONTHS': new_accts_in_last_six_months,
                    'DELINQUENT_ACCTS_IN_LAST_SIX_MONTHS': delinquent_accts_in_last_six_months,
                    'AVERAGE_ACCT_AGE': average_acct_age, 'CREDIT_HISTORY_LENGTH': credit_history_length, 'NO_OF_INQUIRIES': no_of_inquiries
                }

                features = pd.DataFrame(data, index=[0])
                return features
            df = user_input_features()
        return df,uploaded_file
       
    def display_user_input_parameters_NSD():  
        # Collects user input features into dataframe
        st.sidebar.header('User Input Parameters')
        st.sidebar.markdown("""
        [Example of NSD input file](https://github.com/amazon-science/fraud-dataset-benchmark#data-sources)
        """)
        uploaded_file = st.sidebar.file_uploader("Upload your input CSV file for NSD", type=["csv"])
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
        else:
            def user_input_features():
                Index      = st.sidebar.slider('Index', 0,   1296674, 500000 )
                trans_date_trans_time = st.sidebar.slider('trans date trans time', 0, 1819550, 700000 )
                cc_num     = st.sidebar.slider('cc num', 0, 5000000000000000, 2500000000000000 )
                merchant   = st.sidebar.slider('merchant', 0, 692, 250 )
                category   = st.sidebar.slider('category', 0, 5000000000000000, 2500000000000000 )
                amt        = st.sidebar.slider('amt', 1, 692 , 300 )
                first      = st.sidebar.slider('first', 0,  354,  200 )
                last       = st.sidebar.slider('last', 0, 485, 300 )
                gender     = st.sidebar.slider('gender', 0, 1, 1 )
                street     = st.sidebar.slider('street', 0, 998, 500 )
                city       = st.sidebar.slider('city', 0, 905, 500 )
                state      = st.sidebar.slider('state', 0, 5, 3 )
                zip        = st.sidebar.slider('zip', 1257, 99921, 50000 )
                lat        = st.sidebar.slider('lat', 21, 67, 50 )
                long       = st.sidebar.slider('long', -166, -68, -100 )
                city_pop   = st.sidebar.slider('city pop', 23, 2906700, 2000000 )
                job        = st.sidebar.slider('job', 0,  496, 200 )
                dob        = st.sidebar.slider('dob', 0, 983, 500 )
                trans_num  = st.sidebar.slider('trans_num', 0, 1852393, 500000 )
                unix_time  = st.sidebar.slider('unix time', 1325376000, 1388534000, 1350000000 )
                merch_lat  = st.sidebar.slider('merch lat', 20, 70, 50 )
                merch_long = st.sidebar.slider('merch long', -167, -67, -100 )
                
                data = {
                        'Index':Index, 'trans_date_trans_time':trans_date_trans_time, 'cc_num':cc_num, 'merchant':merchant, 'category':category, 'amt':amt, 
                        'first':first, 'last':last, 'gender':gender, 'street':street, 'city':city, 'state':state, 'zip':zip, 'lat':lat,
                        'long':long, 'city_pop':city_pop, 'job':job, 'dob':dob, 'trans_num':trans_num, 'unix_time':unix_time, 
                        'merch_lat':merch_lat, 'merch_long':merch_long 
                        }
                features = pd.DataFrame(data, index=[0])
                return features
            df = user_input_features()
        return df,uploaded_file

    def display_user_input_parameters_PS17():  
        # Collects user input features into dataframe
        st.sidebar.header('User Input Parameters')
        st.sidebar.markdown("""
        [Example of PS17 input file](https://www.kaggle.com/datasets/ealaxi/paysim1)
        """)
        uploaded_file = st.sidebar.file_uploader("Upload your input CSV file for PS17", type=["csv"])
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
        else:
            def user_input_features():
                  
                step = st.sidebar.slider('step', 1, 743, 500 )
                type = st.sidebar.slider('type', 0, 4, 2 )
                amount = st.sidebar.slider('amount', 0, 92445520, 20000000 )
                nameOrig = st.sidebar.slider('nameOrig', 0, 6353306, 3000000 )
                oldbalanceOrg = st.sidebar.slider('oldbalanceOrg', 0, 59585040, 30000000 )
                newbalanceOrig = st.sidebar.slider('newbalanceOrig', 0, 59585040,  30000000 )
                nameDest = st.sidebar.slider('nameDest', 0, 49585040, 25000000 )
                oldbalanceDest = st.sidebar.slider('oldbalanceDest', 0, 356015900, 150000000 )
                newbalanceDest = st.sidebar.slider('newbalanceDest', 0, 356179300, 150000000 )
                isFlaggedFraud = st.sidebar.slider('isFlaggedFraud', 0, 1, 0 )
                
                data = {
                        'step':step, 'type':type, 'amount':amount, 'nameOrig':nameOrig, 'oldbalanceOrg':oldbalanceOrg, 
                        'newbalanceOrig':newbalanceOrig, 'nameDest':nameDest, 'oldbalanceDest':oldbalanceDest, 
                        'newbalanceDest':newbalanceDest ,'isFlaggedFraud':isFlaggedFraud, 
                        }
                features = pd.DataFrame(data, index=[0])
                return features
            df = user_input_features()
        return df,uploaded_file
    
    # Define a function to apply the model and display the predictions
    def apply_model_and_display(df,load_clf, method_name):
        if df is not None:
            load_clf = pickle.load(open(f'{load_clf}', 'rb')) 
            prediction = load_clf.predict(df)
            prediction_proba = load_clf.predict_proba(df)
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"<h3 style='color: green;'>Prediction - {method_name}</h3>", unsafe_allow_html=True)
                Classes = np.array(['NonFraud (0)', 'Fraud (1)'])
                st.write(Classes[prediction])
            with col2:
                st.markdown("<h3 style='color: Blue;'>Prediction Probability</h3>", unsafe_allow_html=True)
                st.write(prediction_proba)
        else:
            st.write('Data is None. Please make sure to upload a valid CSV file.')

    # Define function to choose dataset and call corresponding user input function
    def choose_dataset():
        dataset_choice = st.sidebar.radio("Select Dataset", ['Credit-Card Dataset', 'Alice Dataset', 'IEEE dataset', 
                                                             'LOAN dataset', 'NSD dataset', 'PaySim17 dataset'])
        if dataset_choice     == 'Credit-Card Dataset':
            df, uploaded_file = display_user_input_parameters_CC()
            return df, uploaded_file, dataset_choice
        elif dataset_choice   == 'Alice Dataset':
            df, uploaded_file = display_user_input_parameters_CMIYC()
            return df, uploaded_file, dataset_choice
        elif dataset_choice   == 'IEEE dataset':
            df, uploaded_file = display_user_input_parameters_IEEE()
            return df, uploaded_file, dataset_choice
        elif dataset_choice   == 'LOAN dataset':
            df, uploaded_file = display_user_input_parameters_LOAN()
            return df, uploaded_file, dataset_choice
        elif dataset_choice   == 'NSD dataset':
            df, uploaded_file = display_user_input_parameters_NSD()
            return df, uploaded_file, dataset_choice
        else:
            df, uploaded_file = display_user_input_parameters_PS17()
            return df, uploaded_file, dataset_choice
 
    header()
    # Create a function for the page
    def LR():
        df, uploaded_file, dataset_choice = choose_dataset()
        st.write(f"""
        # Simple Fraud Prediction App Using Imbalanced Data With {dataset_choice}
        This app predicts the transaction type! (Fraud, NonFraud)
        """)
        if uploaded_file is not None:
            st.write(df)
        else:
            st.write('Awaiting CSV file to be uploaded. Currently using example input parameters (shown in left sidebar).')
            st.write(df)

        # st.subheader('Logistic Regression Algorithms Results (Predictions) ')
        st.markdown("<h3 style='color: Brown;'>Logistic Regression Algorithms Results (Predictions)</h3>", unsafe_allow_html=True)

        # Apply the function for each method
        if   dataset_choice == 'Credit-Card Dataset':
            methods_LR = [
                ('CC/CC_LogisticRegression_RUS.pkl', 'RUS'), ('CC/CC_LogisticRegression_ROS.pkl', 'ROS'),
                ('CC/CC_LogisticRegression_SMOTE.pkl', 'SMOTE'), ('CC/CC_LogisticRegression_SMOTEENN.pkl', 'SMOTEENN'),
                ('CC/CC_LogisticRegression_BSMOTE.pkl', 'BSMOTE'), ('CC/CC_LogisticRegression_ADASYN.pkl', 'ADASYN')
            ]
        elif dataset_choice == 'Alice Dataset':
            methods_LR = [
                ('CMIYC/CMIYC_LogisticRegression_RUS.pkl', 'RUS'), ('CMIYC/CMIYC_LogisticRegression_ROS.pkl', 'ROS'),
                ('CMIYC/CMIYC_LogisticRegression_SMOTE.pkl', 'SMOTE'), ('CMIYC/CMIYC_LogisticRegression_SMOTEENN.pkl', 'SMOTEENN'),
                ('CMIYC/CMIYC_LogisticRegression_BSMOTE.pkl', 'BSMOTE'), ('CMIYC/CMIYC_LogisticRegression_ADASYN.pkl', 'ADASYN')
            ]
        elif dataset_choice == 'IEEE dataset':
             methods_LR = [
                ('IEEE/IEEE_LogisticRegression_RUS.pkl', 'RUS'), ('IEEE/IEEE_LogisticRegression_ROS.pkl', 'ROS'),
                ('IEEE/IEEE_LogisticRegression_SMOTE.pkl', 'SMOTE'), ('IEEE/IEEE_LogisticRegression_SMOTEENN.pkl', 'SMOTEENN'),
                ('IEEE/IEEE_LogisticRegression_BSMOTE.pkl', 'BSMOTE'), ('IEEE/IEEE_LogisticRegression_ADASYN.pkl', 'ADASYN')
             ]
        elif dataset_choice == 'LOAN dataset':
             methods_LR = [
                ('LOAN/LOAN_LogisticRegression_RUS.pkl', 'RUS'), ('LOAN/LOAN_LogisticRegression_ROS.pkl', 'ROS'),
                ('LOAN/LOAN_LogisticRegression_SMOTE.pkl', 'SMOTE'), ('LOAN/LOAN_LogisticRegression_SMOTEENN.pkl', 'SMOTEENN'),
                ('LOAN/LOAN_LogisticRegression_BSMOTE.pkl', 'BSMOTE'), ('LOAN/LOAN_LogisticRegression_ADASYN.pkl', 'ADASYN')
             ]
        elif dataset_choice == 'NSD dataset':
            methods_LR = [
                ('NSD/NSD_LogisticRegression_RUS.pkl', 'RUS'), ('NSD/NSD_LogisticRegression_ROS.pkl', 'ROS'),
                ('NSD/NSD_LogisticRegression_SMOTE.pkl', 'SMOTE'), ('NSD/NSD_LogisticRegression_SMOTEENN.pkl', 'SMOTEENN'),
                ('NSD/NSD_LogisticRegression_BSMOTE.pkl', 'BSMOTE'), ('NSD/NSD_LogisticRegression_ADASYN.pkl', 'ADASYN')
             ]
        else:
            methods_LR = [
                ('PS17/PS17_LogisticRegression_RUS.pkl', 'RUS'), ('PS17/PS17_LogisticRegression_ROS.pkl', 'ROS'),
                ('PS17/PS17_LogisticRegression_SMOTE.pkl', 'SMOTE'), ('PS17/PS17_LogisticRegression_SMOTEENN.pkl', 'SMOTEENN'),
                ('PS17/PS17_LogisticRegression_BSMOTE.pkl', 'BSMOTE'), ('PS17/PS17_LogisticRegression_ADASYN.pkl', 'ADASYN')
             ]

        for clf, method_name in methods_LR:
            apply_model_and_display(df, clf, method_name)
        
    # Create a function for the page
    def DT():
    
        # Collects user input features into dataframe
        df, uploaded_file, dataset_choice = choose_dataset()
        st.write(f"""
        # Simple Fraud Prediction App Using Imbalanced Data With {dataset_choice}
        This app predicts the transaction type! (Fraud, NonFraud)
        """)

        st.subheader('User Input parameters')

        if uploaded_file is not None:
            st.write(df)
        else:
            st.write('Awaiting CSV file to be uploaded. Currently using example input parameters (shown in left sidebar).')
            st.write(df)

        st.markdown("<h3 style='color: Brown;'>Decision Tree Classifier Algorithms Results (Predictions)</h3>", unsafe_allow_html=True)

        # Apply the function for each method
        if   dataset_choice == 'Credit-Card Dataset':
            methods_DT = [
                ('CC/CC_DecisionTreeClassifier_RUS.pkl', 'RUS'), ('CC/CC_DecisionTreeClassifier_ROS.pkl', 'ROS'),
                ('CC/CC_DecisionTreeClassifier_SMOTE.pkl', 'SMOTE'), ('CC/CC_DecisionTreeClassifier_SMOTEENN.pkl', 'SMOTEENN'),
                ('CC/CC_DecisionTreeClassifier_BSMOTE.pkl', 'BSMOTE'), ('CC/CC_DecisionTreeClassifier_ADASYN.pkl', 'ADASYN')
            ]
        elif dataset_choice == 'Alice Dataset':
            methods_DT = [
                ('CMIYC/CMIYC_DecisionTreeClassifier_RUS.pkl', 'RUS'), ('CMIYC/CMIYC_DecisionTreeClassifier_ROS.pkl', 'ROS'),
                ('CMIYC/CMIYC_DecisionTreeClassifier_SMOTE.pkl', 'SMOTE'), ('CMIYC/CMIYC_DecisionTreeClassifier_SMOTEENN.pkl', 'SMOTEENN'),
                ('CMIYC/CMIYC_DecisionTreeClassifier_BSMOTE.pkl', 'BSMOTE'), ('CMIYC/CMIYC_DecisionTreeClassifier_ADASYN.pkl', 'ADASYN')
            ]
        elif dataset_choice == 'IEEE dataset':
             methods_DT = [
                ('IEEE/IEEE_DecisionTreeClassifier_RUS.pkl', 'RUS'), ('IEEE/IEEE_DecisionTreeClassifier_ROS.pkl', 'ROS'),
                ('IEEE/IEEE_DecisionTreeClassifier_SMOTE.pkl', 'SMOTE'), ('IEEE/IEEE_DecisionTreeClassifier_SMOTEENN.pkl', 'SMOTEENN'),
                ('IEEE/IEEE_DecisionTreeClassifier_BSMOTE.pkl', 'BSMOTE'), ('IEEE/IEEE_DecisionTreeClassifier_ADASYN.pkl', 'ADASYN')
             ]
        elif dataset_choice == 'LOAN dataset':
             methods_DT = [
                ('LOAN/LOAN_DecisionTreeClassifier_RUS.pkl', 'RUS'), ('LOAN/LOAN_DecisionTreeClassifier_ROS.pkl', 'ROS'),
                ('LOAN/LOAN_DecisionTreeClassifier_SMOTE.pkl', 'SMOTE'), ('LOAN/LOAN_DecisionTreeClassifier_SMOTEENN.pkl', 'SMOTEENN'),
                ('LOAN/LOAN_DecisionTreeClassifier_BSMOTE.pkl', 'BSMOTE'), ('LOAN/LOAN_DecisionTreeClassifier_ADASYN.pkl', 'ADASYN')
             ]
        elif dataset_choice == 'NSD dataset':
             methods_DT = [
                ('NSD/NSD_DecisionTreeClassifier_RUS.pkl', 'RUS'), ('NSD/NSD_DecisionTreeClassifier_ROS.pkl', 'ROS'),
                ('NSD/NSD_DecisionTreeClassifier_SMOTE.pkl', 'SMOTE'), ('NSD/NSD_DecisionTreeClassifier_SMOTEENN.pkl', 'SMOTEENN'),
                ('NSD/NSD_DecisionTreeClassifier_BSMOTE.pkl', 'BSMOTE'), ('NSD/NSD_DecisionTreeClassifier_ADASYN.pkl', 'ADASYN')
             ]
        else:
             methods_DT = [
                ('PS17/PS17_DecisionTreeClassifier_RUS.pkl', 'RUS'), ('PS17/PS17_DecisionTreeClassifier_ROS.pkl', 'ROS'),
                ('PS17/PS17_DecisionTreeClassifier_SMOTE.pkl', 'SMOTE'), ('PS17/PS17_DecisionTreeClassifier_SMOTEENN.pkl', 'SMOTEENN'),
                ('PS17/PS17_DecisionTreeClassifier_BSMOTE.pkl', 'BSMOTE'), ('PS17/PS17_DecisionTreeClassifier_ADASYN.pkl', 'ADASYN')
             ]
        for clf, method_name in methods_DT:
            apply_model_and_display(df, clf, method_name)
        
    # Create a function for the page
    def RF():
        # Collects user input features into dataframe
        df, uploaded_file, dataset_choice = choose_dataset()
        st.write(f"""
        # Simple Fraud Prediction App Using Imbalanced Data With {dataset_choice}
        This app predicts the transaction type! (Fraud, NonFraud)
        """)

        st.subheader('User Input parameters')

        if uploaded_file is not None:
            st.write(df)
        else:
            st.write('Awaiting CSV file to be uploaded. Currently using example input parameters (shown in left sidebar).')
            st.write(df)

        # st.subheader('Random Forest Classifier Algorithms Results (Predictions) ')
        st.markdown("<h3 style='color: Brown;'>Random Forest Classifier Algorithms Results (Predictions)</h3>", unsafe_allow_html=True)

        # Apply the function for each method
        if   dataset_choice == 'Credit-Card Dataset':
            methods_RF = [
                ('CC/CC_RandomForestClassifier_RUS.pkl', 'RUS'), ('CC/CC_RandomForestClassifier_ROS.pkl', 'ROS'),
                ('CC/CC_RandomForestClassifier_SMOTE.pkl', 'SMOTE'), ('CC/CC_RandomForestClassifier_SMOTEENN.pkl', 'SMOTEENN'),
                ('CC/CC_RandomForestClassifier_BSMOTE.pkl', 'BSMOTE'), ('CC/CC_RandomForestClassifier_ADASYN.pkl', 'ADASYN')
            ]
        elif dataset_choice == 'Alice Dataset':
            methods_RF = [
                (path_models+'/CMIYC/CMIYC_RandomForestClassifier_RUS.pkl', 'RUS'), (path_models+'/CMIYC/CMIYC_RandomForestClassifier_ROS.pkl', 'ROS'),
                (path_models+'/CMIYC/CMIYC_RandomForestClassifier_SMOTE.pkl', 'SMOTE'), (path_models+'/CMIYC/CMIYC_RandomForestClassifier_SMOTEENN.pkl', 'SMOTEENN'),
                (path_models+'/CMIYC/CMIYC_RandomForestClassifier_BSMOTE.pkl', 'BSMOTE'), (path_models+'/CMIYC/CMIYC_RandomForestClassifier_ADASYN.pkl', 'ADASYN')
            ]
        elif dataset_choice == 'IEEE dataset':
             methods_RF = [
                (path_models+'/IEEE/IEEE_RandomForestClassifier_RUS.pkl', 'RUS'), (path_models+'/IEEE/IEEE_RandomForestClassifier_ROS.pkl', 'ROS'),
                (path_models+'/IEEE/IEEE_RandomForestClassifier_SMOTE.pkl', 'SMOTE'), (path_models+'/IEEE/IEEE_RandomForestClassifier_SMOTEENN.pkl', 'SMOTEENN'),
                (path_models+'/IEEE/IEEE_RandomForestClassifier_BSMOTE.pkl', 'BSMOTE'), (path_models+'/IEEE/IEEE_RandomForestClassifier_ADASYN.pkl', 'ADASYN')
             ]
        elif dataset_choice == 'LOAN dataset':
             methods_RF = [
                (path_models+'/LOAN/LOAN_RandomForestClassifier_RUS.pkl', 'RUS'), (path_models+'/LOAN/LOAN_RandomForestClassifier_ROS.pkl', 'ROS'),
                (path_models+'/LOAN/LOAN_RandomForestClassifier_SMOTE.pkl', 'SMOTE'), (path_models+'/LOAN/LOAN_RandomForestClassifier_SMOTEENN.pkl', 'SMOTEENN'),
                (path_models+'/LOAN/LOAN_RandomForestClassifier_BSMOTE.pkl', 'BSMOTE'), (path_models+'/LOAN/LOAN_RandomForestClassifier_ADASYN.pkl', 'ADASYN')
             ]
        elif dataset_choice == 'NSD dataset':
             methods_RF = [
                (path_models+'/NSD/NSD_RandomForestClassifier_RUS.pkl', 'RUS'), (path_models+'/NSD/NSD_RandomForestClassifier_ROS.pkl', 'ROS'),
                (path_models+'/NSD/NSD_RandomForestClassifier_SMOTE.pkl', 'SMOTE'), (path_models+'/NSD/NSD_RandomForestClassifier_SMOTEENN.pkl', 'SMOTEENN'),
                (path_models+'/NSD/NSD_RandomForestClassifier_BSMOTE.pkl', 'BSMOTE'), (path_models+'/NSD/NSD_RandomForestClassifier_ADASYN.pkl', 'ADASYN')
             ]
        else:
             methods_RF = [
                (path_models+'/PS17/PS17_RandomForestClassifier_RUS.pkl', 'RUS'), (path_models+'/PS17/PS17_RandomForestClassifier_ROS.pkl', 'ROS'),
                (path_models+'/PS17/PS17_RandomForestClassifier_SMOTE.pkl', 'SMOTE'), (path_models+'/PS17/PS17_RandomForestClassifier_SMOTEENN.pkl', 'SMOTEENN'),
                (path_models+'/PS17/PS17_RandomForestClassifier_BSMOTE.pkl', 'BSMOTE'), (path_models+'/PS17/PS17_RandomForestClassifier_ADASYN.pkl', 'ADASYN')
             ]
          # else:
          #   st.write(f"""
          #           ## RandomForestClassifier is not used in this simulation because the size of the algorithms is too large (you can run the Web application locally and see the results instead).
          #           """)
          #   methods_RF = [
                
          #   ]

        for clf, method_name in methods_RF:
            apply_model_and_display(df, clf, method_name)
        
    # Create a function for the page
    def XGB():
        # Collects user input features into dataframe
        df, uploaded_file, dataset_choice = choose_dataset()
        st.write(f"""
        # Simple Fraud Prediction App Using Imbalanced Data With {dataset_choice}
        This app predicts the transaction type! (Fraud, NonFraud)
        """)

        if uploaded_file is not None:
            st.write(df)
        else:
            st.write('Awaiting CSV file to be uploaded. Currently using example input parameters (shown in left sidebar).')
            st.write(df)

        # st.subheader('Random Forest Classifier Algorithms Results (Predictions) ')
        st.markdown("<h3 style='color: Brown;'>XGBoost Classifier Algorithms Results (Predictions)</h3>", unsafe_allow_html=True)

        # Apply the function for each method
        if   dataset_choice == 'Credit-Card Dataset':
            methods_XGB = [
                ('CC/CC_XGBClassifier_RUS.pkl', 'RUS'), ('CC/CC_XGBClassifier_ROS.pkl', 'ROS'),
                ('CC/CC_XGBClassifier_SMOTE.pkl', 'SMOTE'), ('CC/CC_XGBClassifier_SMOTEENN.pkl', 'SMOTEENN'),
                ('CC/CC_XGBClassifier_BSMOTE.pkl', 'BSMOTE'), ('CC/CC_XGBClassifier_ADASYN.pkl', 'ADASYN')
            ]
        elif dataset_choice == 'Alice Dataset':
            methods_XGB = [
                ('CMIYC/CMIYC_XGBClassifier_RUS.pkl', 'RUS'), ('CMIYC/CMIYC_XGBClassifier_ROS.pkl', 'ROS'),
                ('CMIYC/CMIYC_XGBClassifier_SMOTE.pkl', 'SMOTE'), ('CMIYC/CMIYC_XGBClassifier_SMOTEENN.pkl', 'SMOTEENN'),
                ('CMIYC/CMIYC_XGBClassifier_BSMOTE.pkl', 'BSMOTE'), ('CMIYC/CMIYC_XGBClassifier_ADASYN.pkl', 'ADASYN')
            ]
        elif dataset_choice == 'IEEE dataset':
             methods_XGB = [
                ('IEEE/IEEE_XGBClassifier_RUS.pkl', 'RUS'), ('IEEE/IEEE_XGBClassifier_ROS.pkl', 'ROS'),
                ('IEEE/IEEE_XGBClassifier_SMOTE.pkl', 'SMOTE'), ('IEEE/IEEE_XGBClassifier_SMOTEENN.pkl', 'SMOTEENN'),
                ('IEEE/IEEE_XGBClassifier_BSMOTE.pkl', 'BSMOTE'), ('IEEE/IEEE_XGBClassifier_ADASYN.pkl', 'ADASYN')
             ]
        elif dataset_choice == 'LOAN dataset':
             methods_XGB = [
                ('LOAN/LOAN_XGBClassifier_RUS.pkl', 'RUS'), ('LOAN/LOAN_XGBClassifier_ROS.pkl', 'ROS'),
                ('LOAN/LOAN_XGBClassifier_SMOTE.pkl', 'SMOTE'), ('LOAN/LOAN_XGBClassifier_SMOTEENN.pkl', 'SMOTEENN'),
                ('LOAN/LOAN_XGBClassifier_BSMOTE.pkl', 'BSMOTE'), ('LOAN/LOAN_XGBClassifier_ADASYN.pkl', 'ADASYN')
             ]
        elif dataset_choice == 'NSD dataset':
             methods_XGB = [
                ('NSD/NSD_XGBClassifier_RUS.pkl', 'RUS'), ('NSD/NSD_XGBClassifier_ROS.pkl', 'ROS'),
                ('NSD/NSD_XGBClassifier_SMOTE.pkl', 'SMOTE'), ('NSD/NSD_XGBClassifier_SMOTEENN.pkl', 'SMOTEENN'),
                ('NSD/NSD_XGBClassifier_BSMOTE.pkl', 'BSMOTE'), ('NSD/NSD_XGBClassifier_ADASYN.pkl', 'ADASYN')
             ]
        else:
             methods_XGB = [
                ('PS17/PS17_XGBClassifier_RUS.pkl', 'RUS'), ('PS17/PS17_XGBClassifier_ROS.pkl', 'ROS'),
                ('PS17/PS17_XGBClassifier_SMOTE.pkl', 'SMOTE'), ('PS17/PS17_XGBClassifier_SMOTEENN.pkl', 'SMOTEENN'),
                ('PS17/PS17_XGBClassifier_BSMOTE.pkl', 'BSMOTE'), ('PS17/PS17_XGBClassifier_ADASYN.pkl', 'ADASYN')
             ]
        for clf, method_name in methods_XGB:
            apply_model_and_display(df, clf, method_name)

    selected_function = st.sidebar.radio("Select Models", ['Logistic Regression', 'Decision Tree Classifier', 'Random Forest Classifier', 'XGBoost Classifier'])

    if selected_function == 'Logistic Regression':
        LR()
    elif selected_function == 'Decision Tree Classifier':
        DT()
    elif selected_function == 'Random Forest Classifier':
        RF()
    elif selected_function == 'XGBoost Classifier':
        XGB()

# Create a function for the Info page
def Info():
    # Create a sidebar
    # Display content for Option 1
    with st.sidebar:
        st.markdown("# Details about trained models")
        # Add sidebar elements
        sidebar_option = st.selectbox("Select a model", ["Methodology", "Dataset info", "LR", "DT","RF", "XGB"])
    # Sidebar option dependent content
    def Methodology():
        header()
        st.write("""
                Here we present the details about models, evaluation metrics and methods used in the simulations.\n
                In our simulations, we employed a variety of models, datasets, evaluation metrics, and methods to ensure a comprehensive analysis of the data. Our primary modeling algorithms were Logistic regression (LR), Decision Tree (DT), Random Forest (RF), XGBoost Classifier (XGB). a versatile ensemble learning technique known for its robustness and ability to handle both classification and regression tasks effectively.\n
                To address potential class imbalance issues in our dataset, we employed several resampling techniques to create balanced training sets. These methods included:\n
                
                - Random Undersampling (RUS): RUS involves reducing the size of the majority class by randomly removing instances. This helps prevent the model from being biased toward the dominant class.

                - Random Oversampling (ROS): ROS, on the other hand, involves increasing the number of instances in the minority class by duplicating or generating synthetic samples. This helps ensure that the model does not ignore the minority class.

                - SMOTE (Synthetic Minority Over-sampling Technique): SMOTE is a popular oversampling technique that generates synthetic examples for the minority class by interpolating between existing instances. This method helps address class imbalance while avoiding overfitting.\n

                - SMOTEENN (SMOTE + Edited Nearest Neighbors): SMOTEENN a hybrid resampling technique that combines the Synthetic Minority Over-sampling Technique (SMOTE) with Edited Nearest Neighbors (ENN). It first applies SMOTE to oversample the minority class by generating synthetic samples, similar to SMOTE. However, it then employs ENN to remove noisy and potentially misclassified examples. This two-step process helps improve the balance of the classes while eliminating potential outliers, resulting in a more robust and balanced dataset.
                
                - BorderlineSMOTE (BSMOTE): BSMOTE is an oversampling technique designed specifically for addressing imbalanced datasets. It focuses on the borderline instances of the minority class, which are samples that are closer to the majority class. BSMOTE generates synthetic examples for these borderline instances, helping to increase the representation of the minority class. This method is effective in improving classification performance for imbalanced datasets without oversaturating the dataset with synthetic samples.
                
                - ADASYN (Adaptive Synthetic Sampling): ADASYN is an adaptive oversampling technique that aims to address class imbalance by generating synthetic samples for the minority class. Unlike fixed oversampling techniques, ADASYN assesses the density distribution of minority class instances. It assigns a higher priority to generating synthetic samples for minority instances that are more challenging to classify, effectively adapting to the local density of the data. This adaptability makes ADASYN suitable for scenarios where class imbalance varies across the dataset.

                To account for potential disparities in the cost associated with different classes or prediction errors, we employed *cost-sensitive learning* techniques. These methods assign different weights to each class or type of misclassification error. This ensures that the model takes into consideration the specific costs involved in its predictions, leading to more realistic and actionable results in real-world scenarios.                        
                                
                To carry out these simulations, we used carefully selected datasets from different sources and covering a variety of domains, including real data, transformed data, simulated synthetic data and anonymised data. These datasets play a crucial role in the quality, accuracy and relevance of the results obtained.
                For further elaboration on these datasets, please navigate to the left sidebar and select the desired dataset.
                """)
        st.write("""
                By utilizing a combination of Logistic regression (LR), Decision Tree (DT), Random Forest (RF), and XGBoost Classifier (XGB) modeling, with resampling techniques (RUS, ROS, and SMOTE, SMOTEENN, BorderlineSMOTE(BSMOTE), ADASYN), and cost-sensitive learning methods, our simulations aimed to provide a robust and holistic assessment of the data, ensuring that our models were capable of handling class imbalances and optimizing their performance for practical applications.
                """) 

    def Info_CC():

        if sidebar_option == "Methodology":
            Methodology()            
      
        elif sidebar_option == "Dataset info":
            header()
            st.write('## Credit-Card Dataset (CC)')
            st.write("""
            CC Dataset (anonymised)
                     
            The dataset contains credit card transactions made in September 2013 by European cardholders. 
            
            This dataset shows transactions that took place over two days, where we have 492 frauds out of 284315 transactions. The dataset is highly unbalanced, with the positive class (frauds) representing 0.1727% of all transactions.   
            It contains only numerical input variables which are the result of a PCA transformation. Unfortunately, for confidentiality reasons, it is not possible to provide the original characteristics and other information about the data.
            The features `V1, V2, ... V28` are the principal components obtained with PCA. The only features that have not been transformed using PCA are `Time` and `Amount`. 
            
            - The `Time` characteristic contains the seconds elapsed between each transaction and the first transaction in the dataset. 
            - The `Amount` characteristic is the amount of the transaction. This feature can be used for cost-sensitive learning based on the example. 
            - The `Class` feature is the target variable and takes the value 1 in case of fraud and 0 otherwise.
            
           The dataset was collected and analysed as part of a research collaboration between Worldline and the Machine Learning Group ([MLG ULB](http://mlg.ulb.ac.be)) of the ULB (Université Libre de Bruxelles) on massive data mining and fraud detection [[More Info]](https://mlg.ulb.ac.be/wordpress/portfolio_page/defeatfraud-assessment-and-validation-of-deep-feature-engineering-and-learning-solutions-for-fraud-detection/).

            Link to dataset: [See here](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) """)
        
        elif sidebar_option == "LR":
            # Display content for Option 1
            header()
            # Display text
            st.markdown('<h3 style="color: green;">Evaluation Metrics Using LogisticRegression and different resampling methods:</h3>', unsafe_allow_html=True)

            ## RUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUS
            st.markdown('<h3 style="color: brown;">RUS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score   |
                |----------------------------------|---------|
                | Matthews Correlation Coefficient | 88.81 % |
                | F1 Score                         | 94.61 % |
                | Accuracy Score                   | 94.40 % |
                | Recall Score                     | 95.18 % |
                | Precision Score                  | 94.04 % |
                | ROC AUC Score                    | 94.38 % |
                | False Positive Rate              | 06.41 % |
                | Negative Predictive Value        | 94.80 % |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 73                 | 5                  |
                | Positive         | 4                  | 79                 |
                """)

            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1_Score | Support |
                |------------------|-----------|--------|----------|---------|
                | 0                | 0.95      | 0.94   | 0.94     | 78      |
                | 1                | 0.94      | 0.95   | 0.95     | 83      |
                |                  |           |        |          |         |
                | **Accuracy**     |           |        | 0.94     | 161     |
                | **Macro Avg**    | 0.94      | 0.94   | 0.94     | 161     |
                | **Weighted Avg** | 0.94      | 0.94   | 0.94     | 161     |
                """)

            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CC/CC_LogisticRegression_RUS.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying RUS resampling")#, use_container_width=True
            


            # ROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOS
            st.markdown('<h3 style="color: brown;">ROS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score   |
                |----------------------------------|---------|
                | Matthews Correlation Coefficient | 86.89 % |
                | F1 Score                         | 93.12 % |
                | Accuracy Score                   | 93.33 % |
                | Recall Score                     | 89.85 % |
                | Precision Score                  | 96.63 % |
                | ROC AUC Score                    | 93.35 % |
                | False Positive Rate              | 03.14 % |
                | Negative Predictive Value        | 90.45 % |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 48737              | 1585               |
                | Positive         | 5142               | 45537              |
                """)

            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1_Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.90      | 0.97   | 0.94     | 50322      |
                | 1                | 0.97      | 0.90   | 0.93     | 50679      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.93     | 101001     |
                | **Macro Avg**    | 0.94      | 0.93   | 0.93     | 101001     |
                | **Weighted Avg** | 0.94      | 0.93   | 0.93     | 101001     |
                """)

            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CC/CC_LogisticRegression_ROS.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying ROS resampling")#, use_container_width=True
            


        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">SMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 95.17 %                 |
                | F1 Score                         | 97.56 %                 |
                | Accuracy Score                   | 97.57 %                 |
                | Recall Score                     | 96.66 %                 |
                | Precision Score                  | 98.47 %                 |
                | ROC AUC Score                    | 97.58 %                 |
                | False Positive Rate              | 01.50 %                 |
                | Negative Predictive Value        | 96.70 %                 |
                """)

                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 49565              | 757                |
                | Positive         | 1688               | 48991              |
                """)

            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1_Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.97      | 0.98   | 0.98     | 50322      |
                | 1                | 0.98      | 0.97   | 0.98     | 50679      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.98     | 101001     |
                | **Macro Avg**    | 0.98      | 0.98   | 0.98     | 101001     |
                | **Weighted Avg** | 0.98      | 0.98   | 0.98     | 101001     |
                """)


            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CC/CC_LogisticRegression_SMOTE.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying SMOTE resampling")#, use_container_width=True
            
        
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTEEEEEEEEEEEEENNNNNNNNNNNNNNNN
            st.markdown('<h3 style="color: brown;">SMOTEENN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 95.72 %                 |
                | F1 Score                         | 97.88 %                 |
                | Accuracy Score                   | 97.86 %                 |
                | Recall Score                     | 97.52 %                 |
                | Precision Score                  | 98.24 %                 |
                | ROC AUC Score                    | 97.86 %                 |
                | False Positive Rate              | 01.79 %                 |
                | Negative Predictive Value        | 97.47 %                 |
                """)

                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 46704              | 851                |
                | Positive         | 1210               | 47569              |
                """)

            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1_Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.97      | 0.98   | 0.98     | 47555      |
                | 1                | 0.98      | 0.98   | 0.98     | 48779      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.98     | 96334      |
                | **Macro Avg**    | 0.98      | 0.98   | 0.98     | 96334      |
                | **Weighted Avg** | 0.98      | 0.98   | 0.98     | 96334      |
                """)


            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CC/CC_LogisticRegression_SMOTEENN.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying SMOTEENN resampling")#, use_container_width=True
        
        
        
        ## BBBBBBBBSMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">BSMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score   |
                |----------------------------------|---------|
                | Matthews Correlation Coefficient | 98.23 % |
                | F1 Score                         | 99.12 % |
                | Accuracy Score                   | 99.11 % |
                | Recall Score                     | 99.20 % |
                | Precision Score                  | 99.03 % |
                | ROC AUC Score                    | 99.11 % |
                | False Positive Rate              | 00.01 % |
                | Negative Predictive Value        | 99.19 % |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 49832              | 490                |
                | Positive         | 405                | 50274              |
                """)

            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1_Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.99      | 0.99   | 0.99     | 50322      |
                | 1                | 0.99      | 0.99   | 0.99     | 50679      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.99     | 101001     |
                | **Macro Avg**    | 0.99      | 0.99   | 0.99     | 101001     |
                | **Weighted Avg** | 0.99      | 0.99   | 0.99     | 101001     |
                """)

            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CC/CC_LogisticRegression_BSMOTE.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying BSMOTE resampling")#, use_container_width=True
            
        
        
        ## AaaaaaaaaaaaaaaaaaaaaaaaaDAaaaaaaaaaaaaaaaaaaaaaSsssssssssYyyyyNnnnn
            st.markdown('<h3 style="color: brown;">ADASYN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score   |
                |----------------------------------|---------|
                | Matthews Correlation Coefficient | 94.80 % |
                | F1 Score                         | 97.36 % |
                | Accuracy Score                   | 97.39 % |
                | Recall Score                     | 96.35 % |
                | Precision Score                  | 98.39 % |
                | ROC AUC Score                    | 97.39 % |
                | False Positive Rate              | 01.56 % |
                | Negative Predictive Value        | 96.43 % |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 49781              | 794                |
                | Positive         | 1841               | 48577              |
                """)

            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1_Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.96      | 0.98   | 0.97     | 50575      |
                | 1                | 0.98      | 0.96   | 0.97     | 50418      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.97     | 100993     |
                | **Macro Avg**    | 0.97      | 0.97   | 0.97     | 100993     |
                | **Weighted Avg** | 0.97      | 0.97   | 0.97     | 100993     |
                """)

            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CC/CC_LogisticRegression_ADASYN.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying ADASYN resampling")#, use_container_width=True
            
        elif sidebar_option == "DT":
            # Display content for Option 1
            header()
            
            # Display text
            st.markdown('<h3 style="color: green;">Evaluation Metrics Using DecisionTreeClassifier and different resampling methods:</h3>', unsafe_allow_html=True)

            ## RUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUS
            st.markdown('<h3 style="color: brown;">RUS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score   |
                |----------------------------------|---------|
                | Matthews Correlation Coefficient | 82.78 % |
                | F1 Score                         | 91.86 % |
                | Accuracy Score                   | 91.30 % |
                | Recall Score                     | 95.18 % |
                | Precision Score                  | 88.76 % |
                | ROC AUC Score                    | 91.18 % |
                | False Positive Rate              | 12.82 % |
                | Negative Predictive Value        | 94.44 % |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 68                 | 10                 |
                | Positive         | 4                  | 79                 |
                """)

            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1_Score | Support |
                |------------------|-----------|--------|----------|---------|
                | 0                | 0.94      | 0.87   | 0.91     | 78      |
                | 1                | 0.89      | 0.95   | 0.92     | 83      |
                |                  |           |        |          |         |
                | **Accuracy**     |           |        | 0.91     | 161     |
                | **Macro Avg**    | 0.92      | 0.91   | 0.91     | 161     |
                | **Weighted Avg** | 0.92      | 0.91   | 0.91     | 161     |
                """)

            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CC/CC_DecisionTreeClassifier_RUS.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying RUS resampling")#, use_container_width=True
            


            # ROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOS
            st.markdown('<h3 style="color: brown;">ROS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score   |
                |----------------------------------|---------|
                | Matthews Correlation Coefficient | 99.97 % |
                | F1 Score                         | 99.99 % |
                | Accuracy Score                   | 99.99 % |
                | Recall Score                     | 100.0 % |
                | Precision Score                  | 99.97 % |
                | ROC AUC Score                    | 99.99 % |
                | False Positive Rate              | 0.003 % |
                | Negative Predictive Value        | 100.0 % |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 50307              | 15                 |
                | Positive         | 0                  | 50679              |
                """)

            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1_Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 50322      |
                | 1                | 1.00      | 1.00   | 1.00     | 50679      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 101001     |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 101001     |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 101001     |
                """)

            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CC/CC_DecisionTreeClassifier_ROS.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying ROS resampling")#, use_container_width=True
            


        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">SMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 99.76 %                 |
                | F1 Score                         | 99.88 %                 |
                | Accuracy Score                   | 99.88 %                 |
                | Recall Score                     | 99.94 %                 |
                | Precision Score                  | 99.82 %                 |
                | ROC AUC Score                    | 99.88 %                 |
                | False Positive Rate              | 00.18 %                 |
                | Negative Predictive Value        | 99.94 %                 |
                """)

                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 50231              | 91                 |
                | Positive         | 32                 | 50647              |
                """)

            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 50322      |
                | 1                | 1.00      | 1.00   | 1.00     | 50679      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 101001     |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 101001     |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 101001     |
                """)


            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CC/CC_DecisionTreeClassifier_SMOTE.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying SMOTE resampling")#, use_container_width=True
            
        
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTEEEEEEEEEEEEENNNNNNNNNNNNNNNN
            st.markdown('<h3 style="color: brown;">SMOTEENN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 99.76 %                 |
                | F1 Score                         | 99.88 %                 |
                | Accuracy Score                   | 99.88 %                 |
                | Recall Score                     | 99.94 %                 |
                | Precision Score                  | 99.82 %                 |
                | ROC AUC Score                    | 99.88 %                 |
                | False Positive Rate              | 00.18 %                 |
                | Negative Predictive Value        | 99.93 %                 |
                """)

                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 47468              | 87                 |
                | Positive         | 31                 | 48748              |
                """)

            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 47555      |
                | 1                | 1.00      | 1.00   | 1.00     | 48779      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 96334      |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 96334      |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 96334      |
                """)


            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CC/CC_DecisionTreeClassifier_SMOTEENN.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying SMOTEENN resampling")#, use_container_width=True
        
        
        
        ## BBBBBBBBSMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">BSMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 99.92 %                 |
                | F1 Score                         | 99.96 %                 |
                | Accuracy Score                   | 99.96 %                 |
                | Recall Score                     | 99.98 %                 |
                | Precision Score                  | 99.94 %                 |
                | ROC AUC Score                    | 99.96 %                 |
                | False Positive Rate              | 00.06 %                 |
                | Negative Predictive Value        | 99.98 %                 |
                """)

                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 50290              | 32                 |
                | Positive         | 10                 | 50669              |
                """)

            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 50322      |
                | 1                | 1.00      | 1.00   | 1.00     | 50679      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 101001     |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 101001     |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 101001     |
                """)

            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CC/CC_DecisionTreeClassifier_BSMOTE.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying BSMOTE resampling")#, use_container_width=True
            
        
        
        ## AaaaaaaaaaaaaaaaaaaaaaaaaDAaaaaaaaaaaaaaaaaaaaaaSsssssssssYyyyyNnnnn
            st.markdown('<h3 style="color: brown;">ADASYN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 99.79 %                 |
                | F1 Score                         | 99.89 %                 |
                | Accuracy Score                   | 99.89 %                 |
                | Recall Score                     | 99.93 %                 |
                | Precision Score                  | 99.86 %                 |
                | ROC AUC Score                    | 99.89 %                 |
                | False Positive Rate              | 00.14 %                 |
                | Negative Predictive Value        | 99.93 %                 |
                """)

                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 50504              | 71                 |
                | Positive         | 37                 | 50381              |
                """)

            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 50575      |
                | 1                | 1.00      | 1.00   | 1.00     | 50418      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 100993     |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 100993     |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 100993     |
                """)


            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CC/CC_DecisionTreeClassifier_ADASYN.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying ADASYN resampling")#, use_container_width=True

        elif sidebar_option == "RF":
            # Display content for Option 1
            header()
            
            # Display text
            st.markdown('<h3 style="color: green;">Evaluation Metrics Using RandomForestClassifier and different resampling methods:</h3>', unsafe_allow_html=True)

            ## RUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUS
            st.markdown('<h3 style="color: brown;">RUS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score   |
                |----------------------------------|---------|
                | Matthews Correlation Coefficient | 93.86 % |
                | F1 Score                         | 96.93 % |
                | Accuracy Score                   | 96.89 % |
                | Recall Score                     | 95.18 % |
                | Precision Score                  | 98.75 % |
                | ROC AUC Score                    | 96.95 % |
                | False Positive Rate              | 01.28 % |
                | Negative Predictive Value        | 95.06 % |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 77                 | 1                  |
                | Positive         | 4                  | 79                 |
                """)

            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1_Score | Support |
                |------------------|-----------|--------|----------|---------|
                | 0                | 0.95      | 0.99   | 0.97     | 78      |
                | 1                | 0.99      | 0.95   | 0.97     | 83      |
                |                  |           |        |          |         |
                | **Accuracy**     |           |        | 0.97     | 161     |
                | **Macro Avg**    | 0.97      | 0.97   | 0.97     | 161     |
                | **Weighted Avg** | 0.97      | 0.97   | 0.97     | 161     |
                """)

            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CC/CC_RandomForestClassifier_RUS.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying RUS resampling")#, use_container_width=True
            


            # ROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOS
            st.markdown('<h3 style="color: brown;">ROS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score   |
                |----------------------------------|---------|
                | Matthews Correlation Coefficient | 99.99 % |
                | F1 Score                         | 99.99 % |
                | Accuracy Score                   | 99.99 % |
                | Recall Score                     | 100.0 % |
                | Precision Score                  | 99.99 % |
                | ROC AUC Score                    | 99.99 % |
                | False Positive Rate              | 0.008 % |
                | Negative Predictive Value        | 100.0 % |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 50318              | 4                  |
                | Positive         | 0                  | 50679              |
                """)

            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1_Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 50322      |
                | 1                | 1.00      | 1.00   | 1.00     | 50679      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 101001     |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 101001     |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 101001     |
                """)

            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CC/CC_RandomForestClassifier_ROS.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying ROS resampling")#, use_container_width=True
            


        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">SMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score   |
                |----------------------------------|---------|
                | Matthews Correlation Coefficient | 99.98 % |
                | F1 Score                         | 99.99 % |
                | Accuracy Score                   | 99.99 % |
                | Recall Score                     | 100.0 % |
                | Precision Score                  | 99.98 % |
                | ROC AUC Score                    | 99.99 % |
                | False Positive Rate              | 0.014 % |
                | Negative Predictive Value        | 100.0 % |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 50315              | 7                 |
                | Positive         | 0                  | 50679              |
                """)

            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1_Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 50322      |
                | 1                | 1.00      | 1.00   | 1.00     | 50679      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 101001     |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 101001     |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 101001     |
                """)

            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CC/CC_RandomForestClassifier_SMOTE.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying SMOTE resampling")#, use_container_width=True
            
        
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTEEEEEEEEEEEEENNNNNNNNNNNNNNNN
            st.markdown('<h3 style="color: brown;">SMOTEENN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score   |
                |----------------------------------|---------|
                | Matthews Correlation Coefficient | 99.97 % |
                | F1 Score                         | 99.98 % |
                | Accuracy Score                   | 99.98 % |
                | Recall Score                     | 99.98 % |
                | Precision Score                  | 99.98 % |
                | ROC AUC Score                    | 99.98 % |
                | False Positive Rate              | 0.019 % |
                | Negative Predictive Value        | 99.99 % |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 47546              | 9                  |
                | Positive         | 5                  | 48774              |
                """)

            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1_Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 47555      |
                | 1                | 1.00      | 1.00   | 1.00     | 48779      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 96334      |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 96334      |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 96334      |
                """)

            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CC/CC_RandomForestClassifier_SMOTEENN.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying SMOTEENN resampling")#, use_container_width=True
        
        
        
        ## BBBBBBBBSMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">BSMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score   |
                |----------------------------------|---------|
                | Matthews Correlation Coefficient | 99.98 % |
                | F1 Score                         | 99.99 % |
                | Accuracy Score                   | 99.99 % |
                | Recall Score                     | 99.99 % |
                | Precision Score                  | 99.99 % |
                | ROC AUC Score                    | 99.99 % |
                | False Positive Rate              | 0.008 % |
                | Negative Predictive Value        | 99.99 % |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 50318              | 4                  |
                | Positive         | 5                  | 50674              |
                """)

            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1_Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 50322      |
                | 1                | 1.00      | 1.00   | 1.00     | 50679      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 101001     |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 101001     |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 101001     |
                """)

            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CC/CC_RandomForestClassifier_BSMOTE.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying BSMOTE resampling")#, use_container_width=True
            
        
        
        ## AaaaaaaaaaaaaaaaaaaaaaaaaDAaaaaaaaaaaaaaaaaaaaaaSsssssssssYyyyyNnnnn
            st.markdown('<h3 style="color: brown;">ADASYN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score   |
                |----------------------------------|---------|
                | Matthews Correlation Coefficient | 99.98 % |
                | F1 Score                         | 99.99 % |
                | Accuracy Score                   | 99.99 % |
                | Recall Score                     | 100.0 % |
                | Precision Score                  | 99.99 % |
                | ROC AUC Score                    | 99.99 % |
                | False Positive Rate              | 0.014 % |
                | Negative Predictive Value        | 100.0 % |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 50568              | 7                  |
                | Positive         | 0                  | 50418              |
                """)

            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1_Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 50575      |
                | 1                | 1.00      | 1.00   | 1.00     | 50418      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 100993     |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 100993     |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 100993     |
                """)

            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CC/CC_RandomForestClassifier_ADASYN.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying ADASYN resampling")#, use_container_width=True
            
        elif sidebar_option == "XGB":
            # Display content for Option 2
            header()
                     
            # Display text
            st.markdown('<h3 style="color: green;">Evaluation Metrics Using XGBClassifier and different resampling methods:</h3>', unsafe_allow_html=True)

            ## RUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUS
            st.markdown('<h3 style="color: brown;">RUS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 92.54 %                 |
                | F1 Score                         | 96.39 %                 |
                | Accuracy Score                   | 96.27 %                 |
                | Recall Score                     | 96.39 %                 |
                | Precision Score                  | 96.39 %                 |
                | ROC AUC Score                    | 96.27 %                 |
                | False Positive Rate              | 03.85 %                 |
                | Negative Predictive Value        | 96.15 %                 |
                """)

                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 75                 | 3                  |
                | Positive         | 3                  | 80                 |
                """)

            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.96      | 0.96   | 0.96     | 78         |
                | 1                | 0.96      | 0.96   | 0.96     | 83         |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.96     | 161        |
                | **Macro Avg**    | 0.96      | 0.96   | 0.96     | 161        |
                | **Weighted Avg** | 0.96      | 0.96   | 0.96     | 161        |
                """)

            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CC/CC_XGBClassifier_RUS.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying RUS resampling")#, use_container_width=True
            


            # ROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOS
            st.markdown('<h3 style="color: brown;">ROS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 99.98 %                 |
                | F1 Score                         | 99.99 %                 |
                | Accuracy Score                   | 99.99 %                 |
                | Recall Score                     | 100.0 %                 |
                | Precision Score                  | 99.98 %                 |
                | ROC AUC Score                    | 99.99 %                 |
                | False Positive Rate              | 00.02 %                 |
                | Negative Predictive Value        | 100.0 %                 |
                """)

                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 50314              | 8                  |
                | Positive         | 0                  | 50679              |
                """)

            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 50322      |
                | 1                | 1.00      | 1.00   | 1.00     | 50679      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 101001     |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 101001     |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 101001     |
                """)

            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CC/CC_XGBClassifier_ROS.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying ROS resampling")#, use_container_width=True
            


        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">SMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 99.98 %                 |
                | F1 Score                         | 99.99 %                 |
                | Accuracy Score                   | 99.99 %                 |
                | Recall Score                     | 100.0 %                 |
                | Precision Score                  | 99.98 %                 |
                | ROC AUC Score                    | 99.99 %                 |
                | False Positive Rate              | 00.02 %                 |
                | Negative Predictive Value        | 100.0 %                 |
                """)

                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 50310              | 12                 |
                | Positive         | 0                  | 50679              |
                """)

            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 50322      |
                | 1                | 1.00      | 1.00   | 1.00     | 50679      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 101001     |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 101001     |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 101001     |
                """)

            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CC/CC_XGBClassifier_SMOTE.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying SMOTE resampling")#, use_container_width=True
            
        
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTEEEEEEEEEEEEENNNNNNNNNNNNNNNN
            st.markdown('<h3 style="color: brown;">SMOTEENN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 99.97 %                 |
                | F1 Score                         | 99.98 %                 |
                | Accuracy Score                   | 99.98 %                 |
                | Recall Score                     | 99.99 %                 |
                | Precision Score                  | 99.98 %                 |
                | ROC AUC Score                    | 99.98 %                 |
                | False Positive Rate              | 00.03 %                 |
                | Negative Predictive Value        | 99.99 %                 |
                """)

                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 47541              | 14                 |
                | Positive         | 1                  | 48778              |
                """)

            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 47555      |
                | 1                | 1.00      | 1.00   | 1.00     | 48779      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 96334      |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 96334      |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 96334      |
                """)



            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CC/CC_XGBClassifier_SMOTEENN.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying SMOTEENN resampling")#, use_container_width=True
        
        
        
        ## BBBBBBBBSMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">BSMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 99.97 %                 |
                | F1 Score                         | 99.99 %                 |
                | Accuracy Score                   | 99.99 %                 |
                | Recall Score                     | 99.99 %                 |
                | Precision Score                  | 99.98 %                 |
                | ROC AUC Score                    | 99.99 %                 |
                | False Positive Rate              | 00.02 %                 |
                | Negative Predictive Value        | 99.99 %                 |
                """)

                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 50313              | 9                  |
                | Positive         | 5                  | 50674              |
                """)

            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 50322      |
                | 1                | 1.00      | 1.00   | 1.00     | 50679      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 101001     |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 101001     |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 101001     |
                """)


            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CC/CC_XGBClassifier_BSMOTE.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying BSMOTE resampling")#, use_container_width=True
            
        
        
        ## AaaaaaaaaaaaaaaaaaaaaaaaaDAaaaaaaaaaaaaaaaaaaaaaSsssssssssYyyyyNnnnn
            st.markdown('<h3 style="color: brown;">ADASYN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 99.97 %                 |
                | F1 Score                         | 99.99 %                 |
                | Accuracy Score                   | 99.99 %                 |
                | Recall Score                     | 99.99 %                 |
                | Precision Score                  | 99.97 %                 |
                | ROC AUC Score                    | 99.99 %                 |
                | False Positive Rate              | 00.03 %                 |
                | Negative Predictive Value        | 99.99 %                 |
                """)

                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 50561              | 14                 |
                | Positive         | 1                  | 50417              |
                """)

            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 50575      |
                | 1                | 1.00      | 1.00   | 1.00     | 50418      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 100993     |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 100993     |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 100993     |
                """)


            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CC/CC_XGBClassifier_ADASYN.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying ADASYN resampling")#, use_container_width=True
        
    def Info_CMIYC():

        if sidebar_option == "Methodology":
           Methodology()           
      
        elif sidebar_option =='Dataset info':
            header()
            st.write('## Catch-Me-If-You-Can Dataset (CMIYC) / Alice')
            st.write("""
            CMIYC dataset - (anonymised)

            The dataset `train_sessions.csv` contains information about user browsing sessions, the characteristics of which are as follows:

            - site_i: are the identifiers of the sites in this session. The correspondence is given by a dictionary called `site_dic.pkl`.
            
            - time_j : are the timestamps of the visits to the corresponding site.
            
            - target : if this session belongs to Alice.
            
                - The original `train.zip` data can be used to form a different training set from `train_sessions.csv`.

                - This dataset shows transactions that took place over two days, where we have 2297 frauds out of 251264 transactions. The dataset is highly unbalanced, with the positive class (frauds) accounting for 0.91% of all transactions.

                - The "Catch Me If You Can" dataset, also known as the "Alice" dataset, is a well-known dataset in the field of fraud detection. It was published by Kaggle in 2019 as part of a competition to develop models capable of accurately detecting fraudulent transactions in financial data [[Alice]](https://www.kaggle.com/competitions/catch-me-if-you-can-intruder-detection-through-webpage-session-tracking2).
                     
                - The competition was sponsored by the financial institution that provided the data and offered a prize of 25000 $ to the team that developed the most accurate model.

                - The "Catch Me If You Can" dataset was collected by an undisclosed financial institution for fraud detection research purposes. The exact details of the data collection process are not publicly available, but it is likely that the data was collected as part of the normal activities of the financial institution.

                - To protect the privacy of those involved in the transactions, the dataset has been anonymised, meaning that personal information such as `names`, `addresses` and `credit card numbers` has been removed or masked. The dataset also includes a mix of synthetic and real data to ensure the confidentiality and security of the individuals involved.
                             
                """)
        
        elif sidebar_option == "LR":
            # # Display content for Option 1
            header()
            # Display text
            st.markdown('<h3 style="color: green;">Evaluation Metrics Using LogisticRegression and different resampling methods:</h3>', unsafe_allow_html=True)

        # RUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUS
            st.markdown('<h3 style="color: brown;">RUS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)  
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score             |
                |----------------------------------|-------------------|
                | Matthews Correlation Coefficient | 03.94 %           |
                | F1 Score                         | 37.40 %           |
                | Accuracy Score                   | 52.47 %           |
                | Recall Score                     | 29.32 %           |
                | Precision Score                  | 51.61 %           |
                | ROC AUC Score                    | 51.76 %           |
                | False Positive Rate              | 25.80 %           |
                | Negative Predictive Value        | 52.80 %           |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 302                | 105                |
                | Positive         | 270                | 112                |
                """)

             # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1_Score | Support |
                |------------------|-----------|--------|----------|---------|
                | 0                | 0.53      | 0.74   | 0.62     | 407     |
                | 1                | 0.52      | 0.29   | 0.37     | 382     |
                |                  |           |        |          |         |
                | **Accuracy**     |           |        | 0.52     | 789     |
                | **Macro Avg**    | 0.52      | 0.52   | 0.50     | 789     |
                | **Weighted Avg** | 0.52      | 0.52   | 0.50     | 789     |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CMIYC/CMIYC_LogisticRegression_RUS.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying RUS resampling")#, use_container_width=True
            
        # ROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOS
            st.markdown('<h3 style="color: brown;">ROS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 12.14 %                 |
                | F1 Score                         | 56.25 %                 |
                | Accuracy Score                   | 56.06 %                 |
                | Recall Score                     | 56.95 %                 |
                | Precision Score                  | 55.56 %                 |
                | ROC AUC Score                    | 56.07 %                 |
                | False Positive Rate              | 44.82 %                 |
                | Negative Predictive Value        | 56.57 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 21664              | 17596              |
                | Positive         | 16630              | 22003              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.57      | 0.55   | 0.56     | 39260      |
                | 1                | 0.56      | 0.57   | 0.56     | 38633      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.56     | 77893      |
                | **Macro Avg**    | 0.56      | 0.56   | 0.56     | 77893      |
                | **Weighted Avg** | 0.56      | 0.56   | 0.56     | 77893      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CMIYC/CMIYC_LogisticRegression_ROS.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying ROS resampling")#, use_container_width=True
            
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">SMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 05.01 %                 |
                | F1 Score                         | 53.40 %                 |
                | Accuracy Score                   | 52.48 %                 |
                | Recall Score                     | 54.90 %                 |
                | Precision Score                  | 51.99 %                 |
                | ROC AUC Score                    | 52.50 %                 |
                | False Positive Rate              | 49.90 %                 |
                | Negative Predictive Value        | 53.03 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 19671              | 19589              |
                | Positive         | 17423              | 21210              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.53      | 0.50   | 0.52     | 39260      |
                | 1                | 0.52      | 0.55   | 0.53     | 38633      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.52     | 77893      |
                | **Macro Avg**    | 0.53      | 0.53   | 0.52     | 77893      |
                | **Weighted Avg** | 0.53      | 0.52   | 0.52     | 77893      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CMIYC/CMIYC_LogisticRegression_SMOTE.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying SMOTE resampling")#, use_container_width=True
            
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTEEEEEEEEEEEEENNNNNNNNNNNNNNNN
            st.markdown('<h3 style="color: brown;">SMOTEENN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)    
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 05.24 %                 |
                | F1 Score                         | 60.91 %                 |
                | Accuracy Score                   | 53.43 %                 |
                | Recall Score                     | 68.50 %                 |
                | Precision Score                  | 54.83 %                 |
                | ROC AUC Score                    | 52.48 %                 |
                | False Positive Rate              | 63.53 %                 |
                | Negative Predictive Value        | 50.69 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 12392              | 21590              |
                | Positive         | 12055              | 26211              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.51      | 0.36   | 0.42     | 33982      |
                | 1                | 0.55      | 0.68   | 0.61     | 38266      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.53     | 72248      |
                | **Macro Avg**    | 0.53      | 0.52   | 0.52     | 72248      |
                | **Weighted Avg** | 0.53      | 0.53   | 0.52     | 72248      |
    """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CMIYC/CMIYC_LogisticRegression_SMOTEENN.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying SMOTEENN resampling")#, use_container_width=True
             
        # BBBBBBBBSMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">BSMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 08.58 %                 |
                | F1 Score                         | 55.39 %                 |
                | Accuracy Score                   | 54.26 %                 |
                | Recall Score                     | 57.26 %                 |
                | Precision Score                  | 53.64 %                 |
                | ROC AUC Score                    | 54.28 %                 |
                | False Positive Rate              | 48.70 %                 |
                | Negative Predictive Value        | 54.95 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 20141              | 19119              |
                | Positive         | 16510              | 22123              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.55      | 0.51   | 0.53     | 39260      |
                | 1                | 0.54      | 0.57   | 0.55     | 38633      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.54     | 77893      |
                | **Macro Avg**    | 0.54      | 0.54   | 0.54     | 77893      |
                | **Weighted Avg** | 0.54      | 0.54   | 0.54     | 77893      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CMIYC/CMIYC_LogisticRegression_BSMOTE.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying BSMOTE resampling")#, use_container_width=True
                   
        # AaaaaaaaaaaaaaaaaaaaaaaaaDAaaaaaaaaaaaaaaaaaaaaaSsssssssssYyyyyNnnnn
            st.markdown('<h3 style="color: brown;">ADASYN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)           
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 04.98 %                 |
                | F1 Score                         | 53.72 %                 |
                | Accuracy Score                   | 52.47 %                 |
                | Recall Score                     | 55.44 %                 |
                | Precision Score                  | 52.11 %                 |
                | ROC AUC Score                    | 52.48 %                 |
                | False Positive Rate              | 50.47 %                 |
                | Negative Predictive Value        | 52.87 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 19423              | 19789              |
                | Positive         | 17311              | 21534              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.53      | 0.50   | 0.51     | 39212      |
                | 1                | 0.52      | 0.55   | 0.54     | 38845      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.52     | 78057      |
                | **Macro Avg**    | 0.52      | 0.52   | 0.52     | 78057      |
                | **Weighted Avg** | 0.52      | 0.52   | 0.52     | 78057      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CMIYC/CMIYC_LogisticRegression_ADASYN.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying ADASYN resampling")#, use_container_width=True
            
        elif sidebar_option == "DT":
            # Display content for Option 1
            header()
            # Display text
            st.markdown('<h3 style="color: green;">Evaluation Metrics Using DecisionTreeClassifier and different resampling methods:</h3>', unsafe_allow_html=True)

        # RUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUS
            st.markdown('<h3 style="color: brown;">RUS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 38.80 %                 |
                | F1 Score                         | 67.56 %                 |
                | Accuracy Score                   | 69.46 %                 |
                | Recall Score                     | 65.71 %                 |
                | Precision Score                  | 69.53 %                 |
                | ROC AUC Score                    | 69.34 %                 |
                | False Positive Rate              | 27.03 %                 |
                | Negative Predictive Value        | 69.39 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 297                | 110                |
                | Positive         | 131                | 251                |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.69      | 0.73   | 0.71     | 407        |
                | 1                | 0.70      | 0.66   | 0.68     | 382        |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.69     | 789        |
                | **Macro Avg**    | 0.69      | 0.69   | 0.69     | 789        |
                | **Weighted Avg** | 0.69      | 0.69   | 0.69     | 789        |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CMIYC/CMIYC_DecisionTreeClassifier_RUS.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying RUS resampling")#, use_container_width=True
            
        # ROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOS
            st.markdown('<h3 style="color: brown;">ROS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2) 
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 98.91 %                 |
                | F1 Score                         | 99.45 %                 |
                | Accuracy Score                   | 99.45 %                 |
                | Recall Score                     | 100.0 %                 |
                | Precision Score                  | 98.90 %                 |
                | ROC AUC Score                    | 99.45 %                 |
                | False Positive Rate              | 01.09 %                 |
                | Negative Predictive Value        | 100.0 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 38832              | 428                |
                | Positive         | 0                  | 38633              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 0.99   | 0.99     | 39260      |
                | 1                | 0.99      | 1.00   | 0.99     | 38633      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.99     | 77893      |
                | **Macro Avg**    | 0.99      | 0.99   | 0.99     | 77893      |
                | **Weighted Avg** | 0.99      | 0.99   | 0.99     | 77893      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CMIYC/CMIYC_DecisionTreeClassifier_ROS.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying ROS resampling")#, use_container_width=True
            
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">SMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 89.57 %                 |
                | F1 Score                         | 94.79 %                 |
                | Accuracy Score                   | 94.78 %                 |
                | Recall Score                     | 95.69 %                 |
                | Precision Score                  | 93.90 %                 |
                | ROC AUC Score                    | 94.79 %                 |
                | False Positive Rate              | 06.11 %                 |
                | Negative Predictive Value        | 95.67 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 36860              | 2400               |
                | Positive         | 1667               | 36966              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.96      | 0.94   | 0.95     | 39260      |
                | 1                | 0.94      | 0.96   | 0.95     | 38633      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.95     | 77893      |
                | **Macro Avg**    | 0.95      | 0.95   | 0.95     | 77893      |
                | **Weighted Avg** | 0.95      | 0.95   | 0.95     | 77893      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CMIYC/CMIYC_DecisionTreeClassifier_SMOTE.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying SMOTE resampling")#, use_container_width=True
            
        
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTEEEEEEEEEEEEENNNNNNNNNNNNNNNN
            st.markdown('<h3 style="color: brown;">SMOTEENN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 89.13 %                 |
                | F1 Score                         | 94.94 %                 |
                | Accuracy Score                   | 94.58 %                 |
                | Recall Score                     | 95.94 %                 |
                | Precision Score                  | 93.96 %                 |
                | ROC AUC Score                    | 94.50 %                 |
                | False Positive Rate              | 06.95 %                 |
                | Negative Predictive Value        | 95.32 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 31621              | 2361               |
                | Positive         | 1553               | 36713              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.95      | 0.93   | 0.94     | 33982      |
                | 1                | 0.94      | 0.96   | 0.95     | 38266      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.95     | 72248      |
                | **Macro Avg**    | 0.95      | 0.94   | 0.95     | 72248      |
                | **Weighted Avg** | 0.95      | 0.95   | 0.95     | 72248      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CMIYC/CMIYC_DecisionTreeClassifier_SMOTEENN.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying SMOTEENN resampling")#, use_container_width=True
         
        # BBBBBBBBSMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">BSMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 95.62 %                 |
                | F1 Score                         | 97.80 %                 |
                | Accuracy Score                   | 97.80 %                 |
                | Recall Score                     | 98.58 %                 |
                | Precision Score                  | 97.03 %                 |
                | ROC AUC Score                    | 97.81 %                 |
                | False Positive Rate              | 02.97 %                 |
                | Negative Predictive Value        | 98.58 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 38095              | 1165               |
                | Positive         | 547                | 38086              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.99      | 0.97   | 0.98     | 39260      |
                | 1                | 0.97      | 0.99   | 0.98     | 38633      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.98     | 77893      |
                | **Macro Avg**    | 0.98      | 0.98   | 0.98     | 77893      |
                | **Weighted Avg** | 0.98      | 0.98   | 0.98     | 77893      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CMIYC/CMIYC_DecisionTreeClassifier_BSMOTE.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying BSMOTE resampling")#, use_container_width=True
            
         
        # AaaaaaaaaaaaaaaaaaaaaaaaaDAaaaaaaaaaaaaaaaaaaaaaSsssssssssYyyyyNnnnn
            st.markdown('<h3 style="color: brown;">ADASYN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances Metrics")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 89.45 %                 |
                | F1 Score                         | 94.74 %                 |
                | Accuracy Score                   | 94.72 %                 |
                | Recall Score                     | 95.57 %                 |
                | Precision Score                  | 93.92 %                 |
                | ROC AUC Score                    | 94.72 %                 |
                | False Positive Rate              | 06.13 %                 |
                | Negative Predictive Value        | 95.54 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 36809              | 2403               |
                | Positive         | 1719               | 37126              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.96      | 0.94   | 0.95     | 39212      |
                | 1                | 0.94      | 0.96   | 0.95     | 38845      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.95     | 78057      |
                | **Macro Avg**    | 0.95      | 0.95   | 0.95     | 78057      |
                | **Weighted Avg** | 0.95      | 0.95   | 0.95     | 78057      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CMIYC/CMIYC_DecisionTreeClassifier_ADASYN.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying ADASYN resampling")#, use_container_width=True

        elif sidebar_option == "RF":
            # Display content for Option 1
            header()
            # Display text
            st.markdown('<h3 style="color: green;">Evaluation Metrics Using RandomForestClassifier and different resampling methods:</h3>', unsafe_allow_html=True)

        # RUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUS
            st.markdown('<h3 style="color: brown;">RUS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 53.29 %                 |
                | F1 Score                         | 75.60 %                 |
                | Accuracy Score                   | 76.68 %                 |
                | Recall Score                     | 74.61 %                 |
                | Precision Score                  | 76.61 %                 |
                | ROC AUC Score                    | 76.62 %                 |
                | False Positive Rate              | 21.38 %                 |
                | Negative Predictive Value        | 76.74 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 320                | 87                 |
                | Positive         | 97                 | 285                |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.77      | 0.79   | 0.78     | 407        |
                | 1                | 0.77      | 0.75   | 0.76     | 382        |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.77     | 789        |
                | **Macro Avg**    | 0.77      | 0.77   | 0.77     | 789        |
                | **Weighted Avg** | 0.77      | 0.77   | 0.77     | 789        |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CMIYC/CMIYC_RandomForestClassifier_RUS.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying RUS resampling")#, use_container_width=True
            
        # ROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOS
            st.markdown('<h3 style="color: brown;">ROS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 99.97 %                 |
                | F1 Score                         | 99.98 %                 |
                | Accuracy Score                   | 99.98 %                 |
                | Recall Score                     | 100.0 %                 |
                | Precision Score                  | 99.97 %                 |
                | ROC AUC Score                    | 99.98 %                 |
                | False Positive Rate              | 00.03 %                 |
                | Negative Predictive Value        | 100.0 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 39248              | 12                 |
                | Positive         | 0                  | 38633              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 39260      |
                | 1                | 1.00      | 1.00   | 1.00     | 38633      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 77893      |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 77893      |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 77893      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CMIYC/CMIYC_RandomForestClassifier_ROS.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying ROS resampling")#, use_container_width=True
            
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">SMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 97.26 %                 |
                | F1 Score                         | 98.62 %                 |
                | Accuracy Score                   | 98.63 %                 |
                | Recall Score                     | 98.88 %                 |
                | Precision Score                  | 98.37 %                 |
                | ROC AUC Score                    | 98.63 %                 |
                | False Positive Rate              | 01.61 %                 |
                | Negative Predictive Value        | 98.89 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 38626              | 634                |
                | Positive         | 432                | 38201              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.99      | 0.98   | 0.99     | 39260      |
                | 1                | 0.98      | 0.99   | 0.99     | 38633      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.99     | 77893      |
                | **Macro Avg**    | 0.99      | 0.99   | 0.99     | 77893      |
                | **Weighted Avg** | 0.99      | 0.99   | 0.99     | 77893      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CMIYC/CMIYC_RandomForestClassifier_SMOTE.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying SMOTE resampling")#, use_container_width=True
            
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTEEEEEEEEEEEEENNNNNNNNNNNNNNNN
            st.markdown('<h3 style="color: brown;">SMOTEENN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 97.39 %                 |
                | F1 Score                         | 98.78 %                 |
                | Accuracy Score                   | 98.70 %                 |
                | Recall Score                     | 99.11 %                 |
                | Precision Score                  | 98.45 %                 |
                | ROC AUC Score                    | 98.67 %                 |
                | False Positive Rate              | 01.76 %                 |
                | Negative Predictive Value        | 98.99 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 33384              | 598                |
                | Positive         | 342                | 37924              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.99      | 0.98   | 0.99     | 33982      |
                | 1                | 0.98      | 0.99   | 0.99     | 38266      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.99     | 72248      |
                | **Macro Avg**    | 0.99      | 0.99   | 0.99     | 72248      |
                | **Weighted Avg** | 0.99      | 0.99   | 0.99     | 72248      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CMIYC/CMIYC_RandomForestClassifier_SMOTEENN.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying SMOTEENN resampling")#, use_container_width=True
        
                
        # BBBBBBBBSMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">BSMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 98.94 %                 |
                | F1 Score                         | 99.46 %                 |
                | Accuracy Score                   | 99.47 %                 |
                | Recall Score                     | 99.03 %                 |
                | Precision Score                  | 99.90 %                 |
                | ROC AUC Score                    | 99.47 %                 |
                | False Positive Rate              | 00.10 %                 |
                | Negative Predictive Value        | 99.06 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 39221              | 39                 |
                | Positive         | 374                | 38259              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.99      | 1.00   | 0.99     | 39260      |
                | 1                | 1.00      | 0.99   | 0.99     | 38633      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.99     | 77893      |
                | **Macro Avg**    | 0.99      | 0.99   | 0.99     | 77893      |
                | **Weighted Avg** | 0.99      | 0.99   | 0.99     | 77893      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CMIYC/CMIYC_RandomForestClassifier_BSMOTE.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying BSMOTE resampling")#, use_container_width=True
            
           
        ## AaaaaaaaaaaaaaaaaaaaaaaaaDAaaaaaaaaaaaaaaaaaaaaaSsssssssssYyyyyNnnnn
            st.markdown('<h3 style="color: brown;">ADASYN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)           
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 97.45 %                 |
                | F1 Score                         | 98.72 %                 |
                | Accuracy Score                   | 98.72 %                 |
                | Recall Score                     | 98.97 %                 |
                | Precision Score                  | 98.48 %                 |
                | ROC AUC Score                    | 98.72 %                 |
                | False Positive Rate              | 00.02 %                 |
                | Negative Predictive Value        | 98.97 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 38617              | 595                 |
                | Positive         | 402                | 38443               |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.99      | 0.98   | 0.99     | 39212      |
                | 1                | 0.98      | 0.99   | 0.99     | 38845      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.99     | 78057      |
                | **Macro Avg**    | 0.99      | 0.99   | 0.99     | 78057      |
                | **Weighted Avg** | 0.99      | 0.99   | 0.99     | 78057      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CMIYC/CMIYC_RandomForestClassifier_ADASYN.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying ADASYN resampling")#, use_container_width=True
            
        elif sidebar_option == "XGB":
            # Display content for Option 2
            header()                       
            # Display text
            st.markdown('<h3 style="color: green;">Evaluation Metrics Using XGBClassifier and different resampling methods:</h3>', unsafe_allow_html=True)

        # RUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUS
            st.markdown('<h3 style="color: brown;">RUS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 63.96 %                 |
                | F1 Score                         | 81.32 %                 |
                | Accuracy Score                   | 82.00 %                 |
                | Recall Score                     | 80.89 %                 |
                | Precision Score                  | 81.75 %                 |
                | ROC AUC Score                    | 81.97 %                 |
                | False Positive Rate              | 16.95 %                 |
                | Negative Predictive Value        | 82.24 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 338                | 69                 |
                | Positive         | 73                 | 309                |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.82      | 0.83   | 0.83     | 407        |
                | 1                | 0.82      | 0.81   | 0.81     | 382        |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.82     | 789        |
                | **Macro Avg**    | 0.82      | 0.82   | 0.82     | 789        |
                | **Weighted Avg** | 0.82      | 0.82   | 0.82     | 789        |
                """)

            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CMIYC/CMIYC_XGBClassifier_RUS.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying RUS resampling")#, use_container_width=True
            

        # ROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOS
            st.markdown('<h3 style="color: brown;">ROS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)          
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 91.29 %                 |
                | F1 Score                         | 95.64 %                 |
                | Accuracy Score                   | 95.50 %                 |
                | Recall Score                     | 99.48 %                 |
                | Precision Score                  | 92.08 %                 |
                | ROC AUC Score                    | 95.53 %                 |
                | False Positive Rate              | 08.42 %                 |
                | Negative Predictive Value        | 99.45 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 35953              | 3307               |
                | Positive         | 200                | 38433              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.99      | 0.92   | 0.95     | 39260      |
                | 1                | 0.92      | 0.99   | 0.96     | 38633      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.95     | 77893      |
                | **Macro Avg**    | 0.96      | 0.96   | 0.95     | 77893      |
                | **Weighted Avg** | 0.96      | 0.95   | 0.95     | 77893      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CMIYC/CMIYC_XGBClassifier_ROS.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying ROS resampling")#, use_container_width=True
            

        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">SMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)        
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 90.74 %                 |
                | F1 Score                         | 95.39 %                 |
                | Accuracy Score                   | 95.34 %                 |
                | Recall Score                     | 97.12 %                 |
                | Precision Score                  | 93.72 %                 |
                | ROC AUC Score                    | 95.36 %                 |
                | False Positive Rate              | 06.41 %                 |
                | Negative Predictive Value        | 97.06 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 36745              | 2515               |
                | Positive         | 1114               | 37519              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.97      | 0.94   | 0.95     | 39260      |
                | 1                | 0.94      | 0.97   | 0.95     | 38633      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.95     | 77893      |
                | **Macro Avg**    | 0.95      | 0.95   | 0.95     | 77893      |
                | **Weighted Avg** | 0.95      | 0.95   | 0.95     | 77893      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CMIYC/CMIYC_XGBClassifier_SMOTE.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying SMOTE resampling")#, use_container_width=True
            
        
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTEEEEEEEEEEEEENNNNNNNNNNNNNNNN
            st.markdown('<h3 style="color: brown;">SMOTEENN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 90.74 %                 |
                | F1 Score                         | 95.70 %                 |
                | Accuracy Score                   | 95.36 %                 |
                | Recall Score                     | 97.57 %                 |
                | Precision Score                  | 93.90 %                 |
                | ROC AUC Score                    | 95.22 %                 |
                | False Positive Rate              | 07.14 %                 |
                | Negative Predictive Value        | 97.14 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 31557              | 2425               |
                | Positive         | 928                | 37338              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.97      | 0.93   | 0.95     | 33982      |
                | 1                | 0.94      | 0.98   | 0.96     | 38266      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.95     | 72248      |
                | **Macro Avg**    | 0.96      | 0.95   | 0.95     | 72248      |
                | **Weighted Avg** | 0.95      | 0.95   | 0.95     | 72248      |
                """)

            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CMIYC/CMIYC_XGBClassifier_SMOTEENN.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying SMOTEENN resampling")#, use_container_width=True
                      
        # BBBBBBBBSMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">BSMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 95.26 %                 |
                | F1 Score                         | 97.62 %                 |
                | Accuracy Score                   | 97.62 %                 |
                | Recall Score                     | 98.47 %                 |
                | Precision Score                  | 96.79 %                 |
                | ROC AUC Score                    | 97.63 %                 |
                | False Positive Rate              | 03.21 %                 |
                | Negative Predictive Value        | 98.47 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 37999              | 1261               |
                | Positive         | 592                | 38041              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.98      | 0.97   | 0.98     | 39260      |
                | 1                | 0.97      | 0.98   | 0.98     | 38633      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.98     | 77893      |
                | **Macro Avg**    | 0.98      | 0.98   | 0.98     | 77893      |
                | **Weighted Avg** | 0.98      | 0.98   | 0.98     | 77893      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CMIYC/CMIYC_XGBClassifier_BSMOTE.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying BSMOTE resampling")#, use_container_width=True
                
        # AaaaaaaaaaaaaaaaaaaaaaaaaDAaaaaaaaaaaaaaaaaaaaaaSsssssssssYyyyyNnnnn
            st.markdown('<h3 style="color: brown;">ADASYN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2) 
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 90.51 %                 |
                | F1 Score                         | 95.29 %                 |
                | Accuracy Score                   | 95.23 %                 |
                | Recall Score                     | 97.07 %                 |
                | Precision Score                  | 93.58 %                 |
                | ROC AUC Score                    | 95.23 %                 |
                | False Positive Rate              | 06.60 %                 |
                | Negative Predictive Value        | 96.98 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 36625              | 2587               |
                | Positive         | 1140               | 37705              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.97      | 0.93   | 0.95     | 39212      |
                | 1                | 0.94      | 0.97   | 0.95     | 38845      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.95     | 78057      |
                | **Macro Avg**    | 0.95      | 0.95   | 0.95     | 78057      |
                | **Weighted Avg** | 0.95      | 0.95   | 0.95     | 78057      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/CMIYC/CMIYC_XGBClassifier_ADASYN.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying ADASYN resampling")#, use_container_width=True

    def Info_IEEE():

        if sidebar_option == "Methodology":
            Methodology()         
      
        elif sidebar_option =='Dataset info':
            header()
            st.write('## IEEE Dataset')
            st.write("""
            - Dataset description:
                
                This is a competition, the aim of which is to predict the probability of an online transaction being fraudulent, as indicated by the binary target `isFraud`. The data is divided into two files: `identity` and `transactions`, which are linked by `TransactionID`. Not all transactions have the corresponding identity information.

            - Categorical characteristics - Transaction  
               
                - `ProductCD`
        
                - `card1` - `card6`
        
                - `addr1`, `addr2`
        
                - `P_emaildomain`
        
                - `R_emaildomain`
        
                - `M1`  - `M9`
                
            - Categorical characteristics - Identity   
                - `DeviceType`
                
                - `DeviceInfo`
        
                - `id_12` - `id_38`
        
                The TransactionDT feature is a time offset from a given reference date (not an actual timestamp).
            
            - Files  
                
                - `train_transaction`, `identity.csv` : the training set.
                
                - `test_transaction`, `identity.csv` : the test set (predict the `isFraud` value for these observations).
                
                - `sample_submission.csv` : a sample submission file in the correct format.  

                Link to dataset: [See here](https://www.kaggle.com/competitions/ieee-fraud-detection/overview)        
                """)
        
        elif sidebar_option == "LR":
            # # Display content for Option 1
            header()
            # Display text
            st.markdown('<h3 style="color: green;">Evaluation Metrics Using LogisticRegression and different resampling methods:</h3>', unsafe_allow_html=True)

        # RUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUS
            st.markdown('<h3 style="color: brown;">RUS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)  
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 27.49 %                 |
                | F1 Score                         | 61.71 %                 |
                | Accuracy Score                   | 63.61 %                 |
                | Recall Score                     | 58.11 %                 |
                | Precision Score                  | 65.79 %                 |
                | ROC AUC Score                    | 63.66 %                 |
                | False Positive Rate              | 30.79 %                 |
                | Negative Predictive Value        | 61.87 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 670                | 298                |
                | Positive         | 413                | 573                |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.62      | 0.69   | 0.65     | 968        |
                | 1                | 0.66      | 0.58   | 0.62     | 986        |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.64     | 1954       |
                | **Macro Avg**    | 0.64      | 0.64   | 0.64     | 1954       |
                | **Weighted Avg** | 0.64      | 0.64   | 0.64     | 1954       |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/IEEE/IEEE_LogisticRegression_RUS.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying RUS resampling")#, use_container_width=True
            
        # ROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOS
            st.markdown('<h3 style="color: brown;">ROS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 38.08 %                 |
                | F1 Score                         | 66.04 %                 |
                | Accuracy Score                   | 68.69 %                 |
                | Recall Score                     | 60.27 %                 |
                | Precision Score                  | 73.02 %                 |
                | ROC AUC Score                    | 68.77 %                 |
                | False Positive Rate              | 22.72 %                 |
                | Negative Predictive Value        | 65.59 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 8681               | 2552               |
                | Positive         | 4554               | 6908               |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.66      | 0.77   | 0.71     | 11233      |
                | 1                | 0.73      | 0.60   | 0.66     | 11462      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.69     | 22695      |
                | **Macro Avg**    | 0.69      | 0.69   | 0.68     | 22695      |
                | **Weighted Avg** | 0.69      | 0.69   | 0.68     | 22695      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/IEEE/IEEE_LogisticRegression_ROS.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying ROS resampling")#, use_container_width=True
            
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">SMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 32.97 %                 |
                | F1 Score                         | 64.10 %                 |
                | Accuracy Score                   | 66.27 %                 |
                | Recall Score                     | 59.61 %                 |
                | Precision Score                  | 69.31 %                 |
                | ROC AUC Score                    | 66.34 %                 |
                | False Positive Rate              | 26.93 %                 |
                | Negative Predictive Value        | 63.94 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 8208               | 3025               |
                | Positive         | 4629               | 6833               |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.64      | 0.73   | 0.68     | 11233      |
                | 1                | 0.69      | 0.60   | 0.64     | 11462      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.66     | 22695      |
                | **Macro Avg**    | 0.67      | 0.66   | 0.66     | 22695      |
                | **Weighted Avg** | 0.67      | 0.66   | 0.66     | 22695      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/IEEE/IEEE_LogisticRegression_SMOTE.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying SMOTE resampling")#, use_container_width=True
            
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTEEEEEEEEEEEEENNNNNNNNNNNNNNNN
            st.markdown('<h3 style="color: brown;">SMOTEENN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)    
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 44.13 %                 |
                | F1 Score                         | 73.59 %                 |
                | Accuracy Score                   | 72.00 %                 |
                | Recall Score                     | 70.46 %                 |
                | Precision Score                  | 77.02 %                 |
                | ROC AUC Score                    | 72.19 %                 |
                | False Positive Rate              | 26.07 %                 |
                | Negative Predictive Value        | 66.85 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 5211               | 1838               |
                | Positive         | 2584               | 6162               |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.67      | 0.74   | 0.70     | 7049       |
                | 1                | 0.77      | 0.70   | 0.74     | 8746       |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.72     | 15795      |
                | **Macro Avg**    | 0.72      | 0.72   | 0.72     | 15795      |
                | **Weighted Avg** | 0.72      | 0.72   | 0.72     | 15795      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/IEEE/IEEE_LogisticRegression_SMOTEENN.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying SMOTEENN resampling")#, use_container_width=True
             
        # BBBBBBBBSMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">BSMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 44.79 %                 |
                | F1 Score                         | 69.97 %                 |
                | Accuracy Score                   | 72.06 %                 |
                | Recall Score                     | 64.43 %                 |
                | Precision Score                  | 76.54 %                 |
                | ROC AUC Score                    | 72.14 %                 |
                | False Positive Rate              | 20.15 %                 |
                | Negative Predictive Value        | 68.75 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 8970               | 2263               |
                | Positive         | 4077               | 7385               |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.69      | 0.80   | 0.74     | 11233      |
                | 1                | 0.77      | 0.64   | 0.70     | 11462      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.72     | 22695      |
                | **Macro Avg**    | 0.73      | 0.72   | 0.72     | 22695      |
                | **Weighted Avg** | 0.73      | 0.72   | 0.72     | 22695      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/IEEE/IEEE_LogisticRegression_BSMOTE.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying BSMOTE resampling")#, use_container_width=True
                   
        # AaaaaaaaaaaaaaaaaaaaaaaaaDAaaaaaaaaaaaaaaaaaaaaaSsssssssssYyyyyNnnnn
            st.markdown('<h3 style="color: brown;">ADASYN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)           
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 46.11 %                 |
                | F1 Score                         | 70.31 %                 |
                | Accuracy Score                   | 72.67 %                 |
                | Recall Score                     | 64.25 %                 |
                | Precision Score                  | 77.63 %                 |
                | ROC AUC Score                    | 72.73 %                 |
                | False Positive Rate              | 18.78 %                 |
                | Negative Predictive Value        | 69.13 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 9153               | 2117               |
                | Positive         | 4088               | 7348               |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.69      | 0.81   | 0.75     | 11270      |
                | 1                | 0.78      | 0.64   | 0.70     | 11436      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.73     | 22706      |
                | **Macro Avg**    | 0.73      | 0.73   | 0.72     | 22706      |
                | **Weighted Avg** | 0.73      | 0.73   | 0.72     | 22706      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/IEEE/IEEE_LogisticRegression_ADASYN.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying ADASYN resampling")#, use_container_width=True
            
        elif sidebar_option == "DT":
            # Display content for Option 1
            header()
            # Display text
            st.markdown('<h3 style="color: green;">Evaluation Metrics Using DecisionTreeClassifier and different resampling methods:</h3>', unsafe_allow_html=True)

        # RUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUS
            st.markdown('<h3 style="color: brown;">RUS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 68.59 %                 |
                | F1 Score                         | 84.61 %                 |
                | Accuracy Score                   | 84.29 %                 |
                | Recall Score                     | 85.60 %                 |
                | Precision Score                  | 83.65 %                 |
                | ROC AUC Score                    | 84.28 %                 |
                | False Positive Rate              | 17.05 %                 |
                | Negative Predictive Value        | 84.97 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 803                | 165                |
                | Positive         | 142                | 844                |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.85      | 0.83   | 0.84     | 968        |
                | 1                | 0.84      | 0.86   | 0.85     | 986        |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.84     | 1954       |
                | **Macro Avg**    | 0.84      | 0.84   | 0.84     | 1954       |
                | **Weighted Avg** | 0.84      | 0.84   | 0.84     | 1954       |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/IEEE/IEEE_DecisionTreeClassifier_RUS.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying RUS resampling")#, use_container_width=True
            
        # ROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOS
            st.markdown('<h3 style="color: brown;">ROS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2) 
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 96.79 %                 |
                | F1 Score                         | 98.41 %                 |
                | Accuracy Score                   | 98.37 %                 |
                | Recall Score                     | 100.0 %                 |
                | Precision Score                  | 96.87 %                 |
                | ROC AUC Score                    | 98.35 %                 |
                | False Positive Rate              | 03.29 %                 |
                | Negative Predictive Value        | 100.0 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 10863              | 370                |
                | Positive         | 0                  | 11462              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 0.97   | 0.98     | 11233      |
                | 1                | 0.97      | 1.00   | 0.98     | 11462      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.98     | 22695      |
                | **Macro Avg**    | 0.98      | 0.98   | 0.98     | 22695      |
                | **Weighted Avg** | 0.98      | 0.98   | 0.98     | 22695      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/IEEE/IEEE_DecisionTreeClassifier_ROS.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying ROS resampling")#, use_container_width=True
            
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">SMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 94.31 %                 |
                | F1 Score                         | 97.19 %                 |
                | Accuracy Score                   | 97.15 %                 |
                | Recall Score                     | 97.44 %                 |
                | Precision Score                  | 96.94 %                 |
                | ROC AUC Score                    | 97.15 %                 |
                | False Positive Rate              | 03.14 %                 |
                | Negative Predictive Value        | 97.38 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 10880              | 353                |
                | Positive         | 293                | 11169              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.97      | 0.97   | 0.97     | 11233      |
                | 1                | 0.97      | 0.97   | 0.97     | 11462      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.97     | 22695      |
                | **Macro Avg**    | 0.97      | 0.97   | 0.97     | 22695      |
                | **Weighted Avg** | 0.97      | 0.97   | 0.97     | 22695      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/IEEE/IEEE_DecisionTreeClassifier_SMOTE.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying SMOTE resampling")#, use_container_width=True
            
        
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTEEEEEEEEEEEEENNNNNNNNNNNNNNNN
            st.markdown('<h3 style="color: brown;">SMOTEENN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 92.95 %                 |
                | F1 Score                         | 96.86 %                 |
                | Accuracy Score                   | 96.52 %                 |
                | Recall Score                     | 97.00 %                 |
                | Precision Score                  | 96.72 %                 |
                | ROC AUC Score                    | 96.46 %                 |
                | False Positive Rate              | 04.09 %                 |
                | Negative Predictive Value        | 96.27 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 6761               | 288                |
                | Positive         | 262                | 8484               |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.96      | 0.96   | 0.96     | 7049       |
                | 1                | 0.97      | 0.97   | 0.97     | 8746       |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.97     | 15795      |
                | **Macro Avg**    | 0.96      | 0.96   | 0.96     | 15795      |
                | **Weighted Avg** | 0.97      | 0.97   | 0.97     | 15795      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/IEEE/IEEE_DecisionTreeClassifier_SMOTEENN.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying SMOTEENN resampling")#, use_container_width=True
         
        # BBBBBBBBSMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">BSMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 93.82 %                 |
                | F1 Score                         | 96.95 %                 |
                | Accuracy Score                   | 96.91 %                 |
                | Recall Score                     | 97.37 %                 |
                | Precision Score                  | 96.55 %                 |
                | ROC AUC Score                    | 96.91 %                 |
                | False Positive Rate              | 03.55 %                 |
                | Negative Predictive Value        | 97.29 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 10834              | 399                |
                | Positive         | 302                | 11160              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.97      | 0.96   | 0.97     | 11233      |
                | 1                | 0.97      | 0.97   | 0.97     | 11462      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.97     | 22695      |
                | **Macro Avg**    | 0.97      | 0.97   | 0.97     | 22695      |
                | **Weighted Avg** | 0.97      | 0.97   | 0.97     | 22695      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/IEEE/IEEE_DecisionTreeClassifier_BSMOTE.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying BSMOTE resampling")#, use_container_width=True
            
         
        # AaaaaaaaaaaaaaaaaaaaaaaaaDAaaaaaaaaaaaaaaaaaaaaaSsssssssssYyyyyNnnnn
            st.markdown('<h3 style="color: brown;">ADASYN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 93.69 %                 |
                | F1 Score                         | 96.88 %                 |
                | Accuracy Score                   | 96.84 %                 |
                | Recall Score                     | 97.23 %                 |
                | Precision Score                  | 96.53 %                 |
                | ROC AUC Score                    | 96.84 %                 |
                | False Positive Rate              | 03.55 %                 |
                | Negative Predictive Value        | 97.17 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 10870              | 400                |
                | Positive         | 317                | 11119              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.97      | 0.96   | 0.97     | 11270      |
                | 1                | 0.97      | 0.97   | 0.97     | 11436      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.97     | 22706      |
                | **Macro Avg**    | 0.97      | 0.97   | 0.97     | 22706      |
                | **Weighted Avg** | 0.97      | 0.97   | 0.97     | 22706      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/IEEE/IEEE_DecisionTreeClassifier_ADASYN.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying ADASYN resampling")#, use_container_width=True

        elif sidebar_option == "RF":
            # Display content for Option 1
            header()
            # Display text
            st.markdown('<h3 style="color: green;">Evaluation Metrics Using RandomForestClassifier and different resampling methods:</h3>', unsafe_allow_html=True)

        # RUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUS
            st.markdown('<h3 style="color: brown;">RUS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 77.79 %                 |
                | F1 Score                         | 88.67 %                 |
                | Accuracy Score                   | 88.84 %                 |
                | Recall Score                     | 86.51 %                 |
                | Precision Score                  | 90.94 %                 |
                | ROC AUC Score                    | 88.87 %                 |
                | False Positive Rate              | 08.78 %                 |
                | Negative Predictive Value        | 86.91 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 883                | 85                 |
                | Positive         | 133                | 853                |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.87      | 0.91   | 0.89     | 968        |
                | 1                | 0.91      | 0.87   | 0.89     | 986        |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.89     | 1954       |
                | **Macro Avg**    | 0.89      | 0.89   | 0.89     | 1954       |
                | **Weighted Avg** | 0.89      | 0.89   | 0.89     | 1954       |
                """)

            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/IEEE/IEEE_RandomForestClassifier_RUS.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying RUS resampling")#, use_container_width=True
            
        # ROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOS
            st.markdown('<h3 style="color: brown;">ROS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 98.99 %                 |
                | F1 Score                         | 99.50 %                 |
                | Accuracy Score                   | 99.49 %                 |
                | Recall Score                     | 100.0 %                 |
                | Precision Score                  | 99.00 %                 |
                | ROC AUC Score                    | 99.49 %                 |
                | False Positive Rate              | 01.02 %                 |
                | Negative Predictive Value        | 100.0 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 11118              | 115                |
                | Positive         | 0                  | 11462              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 0.99   | 0.99     | 11233      |
                | 1                | 0.99      | 1.00   | 1.00     | 11462      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.99     | 22695      |
                | **Macro Avg**    | 1.00      | 0.99   | 0.99     | 22695      |
                | **Weighted Avg** | 0.99      | 0.99   | 0.99     | 22695      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/IEEE/IEEE_RandomForestClassifier_ROS.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying ROS resampling")#, use_container_width=True
            
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">SMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 96.50 %                 |
                | F1 Score                         | 98.24 %                 |
                | Accuracy Score                   | 98.24 %                 |
                | Recall Score                     | 97.29 %                 |
                | Precision Score                  | 99.22 %                 |
                | ROC AUC Score                    | 98.25 %                 |
                | False Positive Rate              | 00.78 %                 |
                | Negative Predictive Value        | 97.29 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 11145              | 88                 |
                | Positive         | 311                | 11151              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.97      | 0.99   | 0.98     | 11233      |
                | 1                | 0.99      | 0.97   | 0.98     | 11462      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.98     | 22695      |
                | **Macro Avg**    | 0.98      | 0.98   | 0.98     | 22695      |
                | **Weighted Avg** | 0.98      | 0.98   | 0.98     | 22695      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/IEEE/IEEE_RandomForestClassifier_SMOTE.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying SMOTE resampling")#, use_container_width=True
            
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTEEEEEEEEEEEEENNNNNNNNNNNNNNNN
            st.markdown('<h3 style="color: brown;">SMOTEENN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 96.27 %                 |
                | F1 Score                         | 98.30 %                 |
                | Accuracy Score                   | 98.14 %                 |
                | Recall Score                     | 97.28 %                 |
                | Precision Score                  | 99.35 %                 |
                | ROC AUC Score                    | 98.24 %                 |
                | False Positive Rate              | 00.79 %                 |
                | Negative Predictive Value        | 96.71 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 6993               | 56                 |
                | Positive         | 238                | 8508               |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.97      | 0.99   | 0.98     | 7049       |
                | 1                | 0.99      | 0.97   | 0.98     | 8746       |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.98     | 15795      |
                | **Macro Avg**    | 0.98      | 0.98   | 0.98     | 15795      |
                | **Weighted Avg** | 0.98      | 0.98   | 0.98     | 15795      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/IEEE/IEEE_RandomForestClassifier_SMOTEENN.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying SMOTEENN resampling")#, use_container_width=True
    
        # BBBBBBBBSMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">BSMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 96.22 %                 |
                | F1 Score                         | 98.10 %                 |
                | Accuracy Score                   | 98.10 %                 |
                | Recall Score                     | 97.07 %                 |
                | Precision Score                  | 99.15 %                 |
                | ROC AUC Score                    | 98.11 %                 |
                | False Positive Rate              | 00.85 %                 |
                | Negative Predictive Value        | 97.07 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 11138              | 95                 |
                | Positive         | 336                | 11126              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.97      | 0.99   | 0.98     | 11233      |
                | 1                | 0.99      | 0.97   | 0.98     | 11462      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.98     | 22695      |
                | **Macro Avg**    | 0.98      | 0.98   | 0.98     | 22695      |
                | **Weighted Avg** | 0.98      | 0.98   | 0.98     | 22695      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/IEEE/IEEE_RandomForestClassifier_BSMOTE.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying BSMOTE resampling")#, use_container_width=True
            
           
        # AaaaaaaaaaaaaaaaaaaaaaaaaDAaaaaaaaaaaaaaaaaaaaaaSsssssssssYyyyyNnnnn
            st.markdown('<h3 style="color: brown;">ADASYN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)           
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 96.32 %                 |
                | F1 Score                         | 98.14 %                 |
                | Accuracy Score                   | 98.15 %                 |
                | Recall Score                     | 97.09 %                 |
                | Precision Score                  | 99.22 %                 |
                | ROC AUC Score                    | 98.16 %                 |
                | False Positive Rate              | 00.77 %                 |
                | Negative Predictive Value        | 97.11 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 11183              | 87                 |
                | Positive         | 333                | 11103              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.97      | 0.99   | 0.98     | 11270      |
                | 1                | 0.99      | 0.97   | 0.98     | 11436      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.98     | 22706      |
                | **Macro Avg**    | 0.98      | 0.98   | 0.98     | 22706      |
                | **Weighted Avg** | 0.98      | 0.98   | 0.98     | 22706      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/IEEE/IEEE_RandomForestClassifier_ADASYN.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying ADASYN resampling")#, use_container_width=True
            
        elif sidebar_option == "XGB":
            # Display content for Option 2
            header()                     
            # Display text
            st.markdown('<h3 style="color: green;">Evaluation Metrics Using XGBClassifier and different resampling methods:</h3>', unsafe_allow_html=True)

        # RUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUS
            st.markdown('<h3 style="color: brown;">RUS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 82.54 %                 |
                | F1 Score                         | 91.20 %                 |
                | Accuracy Score                   | 91.25 %                 |
                | Recall Score                     | 89.86 %                 |
                | Precision Score                  | 92.58 %                 |
                | ROC AUC Score                    | 91.26 %                 |
                | False Positive Rate              | 07.33 %                 |
                | Negative Predictive Value        | 89.97 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 897                | 71                 |
                | Positive         | 100                | 886                |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.90      | 0.93   | 0.91     | 968        |
                | 1                | 0.93      | 0.90   | 0.91     | 986        |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.91     | 1954       |
                | **Macro Avg**    | 0.91      | 0.91   | 0.91     | 1954       |
                | **Weighted Avg** | 0.91      | 0.91   | 0.91     | 1954       |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/IEEE/IEEE_XGBClassifier_RUS.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying RUS resampling")#, use_container_width=True
            

        # ROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOS
            st.markdown('<h3 style="color: brown;">ROS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)          
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 94.40 %                 |
                | F1 Score                         | 97.24 %                 |
                | Accuracy Score                   | 97.20 %                 |
                | Recall Score                     | 97.61 %                 |
                | Precision Score                  | 96.87 %                 |
                | ROC AUC Score                    | 97.19 %                 |
                | False Positive Rate              | 03.22 %                 |
                | Negative Predictive Value        | 97.54 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 10871              | 362                |
                | Positive         | 274                | 11188              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.98      | 0.97   | 0.97     | 11233      |
                | 1                | 0.97      | 0.98   | 0.97     | 11462      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.97     | 22695      |
                | **Macro Avg**    | 0.97      | 0.97   | 0.97     | 22695      |
                | **Weighted Avg** | 0.97      | 0.97   | 0.97     | 22695      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/IEEE/IEEE_XGBClassifier_ROS.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying ROS resampling")#, use_container_width=True
            

        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">SMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)        
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 97.20 %                 |
                | F1 Score                         | 98.60 %                 |
                | Accuracy Score                   | 98.59 %                 |
                | Recall Score                     | 97.84 %                 |
                | Precision Score                  | 99.37 %                 |
                | ROC AUC Score                    | 98.60 %                 |
                | False Positive Rate              | 00.63 %                 |
                | Negative Predictive Value        | 97.83 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 11162              | 71                 |
                | Positive         | 248                | 11214              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.98      | 0.99   | 0.99     | 11233      |
                | 1                | 0.99      | 0.98   | 0.99     | 11462      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.99     | 22695      |
                | **Macro Avg**    | 0.99      | 0.99   | 0.99     | 22695      |
                | **Weighted Avg** | 0.99      | 0.99   | 0.99     | 22695      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/IEEE/IEEE_XGBClassifier_SMOTE.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying SMOTE resampling")#, use_container_width=True
            
        
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTEEEEEEEEEEEEENNNNNNNNNNNNNNNN
            st.markdown('<h3 style="color: brown;">SMOTEENN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 97.30 %                 |
                | F1 Score                         | 98.78 %                 |
                | Accuracy Score                   | 98.66 %                 |
                | Recall Score                     | 98.22 %                 |
                | Precision Score                  | 99.35 %                 |
                | ROC AUC Score                    | 98.71 %                 |
                | False Positive Rate              | 00.79 %                 |
                | Negative Predictive Value        | 97.82 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 6993               | 56                 |
                | Positive         | 156                | 8590               |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.98      | 0.99   | 0.99     | 7049       |
                | 1                | 0.99      | 0.98   | 0.99     | 8746       |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.99     | 15795      |
                | **Macro Avg**    | 0.99      | 0.99   | 0.99     | 15795      |
                | **Weighted Avg** | 0.99      | 0.99   | 0.99     | 15795      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/IEEE/IEEE_XGBClassifier_SMOTEENN.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying SMOTEENN resampling")#, use_container_width=True
                      
        # BBBBBBBBSMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">BSMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 97.13 %                 |
                | F1 Score                         | 98.56 %                 |
                | Accuracy Score                   | 98.56 %                 |
                | Recall Score                     | 97.78 %                 |
                | Precision Score                  | 99.36 %                 |
                | ROC AUC Score                    | 98.57 %                 |
                | False Positive Rate              | 00.64 %                 |
                | Negative Predictive Value        | 97.77 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 11161              | 72                 |
                | Positive         | 255                | 11207              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.98      | 0.99   | 0.99     | 11233      |
                | 1                | 0.99      | 0.98   | 0.99     | 11462      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.99     | 22695      |
                | **Macro Avg**    | 0.99      | 0.99   | 0.99     | 22695      |
                | **Weighted Avg** | 0.99      | 0.99   | 0.99     | 22695      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/IEEE/IEEE_XGBClassifier_BSMOTE.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying BSMOTE resampling")#, use_container_width=True
                
        # AaaaaaaaaaaaaaaaaaaaaaaaaDAaaaaaaaaaaaaaaaaaaaaaSsssssssssYyyyyNnnnn
            st.markdown('<h3 style="color: brown;">ADASYN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2) 
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 97.12 %                 |
                | F1 Score                         | 98.55 %                 |
                | Accuracy Score                   | 98.56 %                 |
                | Recall Score                     | 97.78 %                 |
                | Precision Score                  | 99.34 %                 |
                | ROC AUC Score                    | 98.56 %                 |
                | False Positive Rate              | 00.66 %                 |
                | Negative Predictive Value        | 97.78 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 11196              | 74                 |
                | Positive         | 254                | 11182              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.98      | 0.99   | 0.99     | 11270      |
                | 1                | 0.99      | 0.98   | 0.99     | 11436      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.99     | 22706      |
                | **Macro Avg**    | 0.99      | 0.99   | 0.99     | 22706      |
                | **Weighted Avg** | 0.99      | 0.99   | 0.99     | 22706      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/IEEE/IEEE_XGBClassifier_ADASYN.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying ADASYN resampling")#, use_container_width=True
        
    def Info_LOAN():

        if sidebar_option == "Methodology":
            Methodology()
                      
        elif sidebar_option =='Dataset info':
            header()
            st.write('## LOAN Dataset')
            st.write("""
            Vehicle Loan Default Prediction (LOAN)

            The task of this dataset is to determine the probability of default on a car loan, in particular the risk of default on the first instalments. on the first instalments. It contains data for 233k loans with a default rate of 21.7%.
                     
            Financial institutions are incurring significant losses due to default on car loans. This has led to a tightening of auto loan underwriting and an increase in auto loan rejection rates. The need for a better credit risk assessment model has also been raised by these institutions. This justifies a study aimed at estimating the determinants of default on car loans.
                     
            A financial institution seeks to accurately predict the probability of the borrower defaulting on a car loan on the due date of the first EMI (Equated Monthly Instalments). 
                
            - The following information about the loan and the borrower is provided:
                     
                - Information about the borrower (demographic data such as age, income, proof of identity, etc).
                        
                - Loan information (disbursement details, amount, EMI, loan-to-value ratio, etc.)
                        
                - Bureau data and history (Bureau score, number of active accounts, status of other loans, credit history, etc). By doing this, we can ensure that customers who are able to repay are not rejected, and we can identify important determinants that can be used to minimise default rates.
            
            - Source license: Unknown
                     
            - Variables: Loanee information, loan information, credit bureau data, and history.
                     
            - Fraud category: Credit Risk
                     
            - Provider: Avik Paul
                     
            - Release date: 2019-11-12
                     
            Link to dataset: [See here](https://www.kaggle.com/avikpaul4u/vehicle-loan-default-prediction) 
                """)
        
        elif sidebar_option == "LR":
            # # Display content for Option 1
            header()
            # Display text
            st.markdown('<h3 style="color: green;">Evaluation Metrics Using LogisticRegression and different resampling methods:</h3>', unsafe_allow_html=True)

        # RUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUS
            st.markdown('<h3 style="color: brown;">RUS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)  
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 12.43 %                 |
                | F1 Score                         | 60.22 %                 |
                | Accuracy Score                   | 56.22 %                 |
                | Recall Score                     | 65.46 %                 |
                | Precision Score                  | 55.76 %                 |
                | ROC AUC Score                    | 56.11 %                 |
                | False Positive Rate              | 53.25 %                 |
                | Negative Predictive Value        | 56.90 %                 |
                """)

                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 3796               | 4323               |
                | Positive         | 2875               | 5448               |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.57      | 0.47   | 0.51     | 8119       |
                | 1                | 0.56      | 0.65   | 0.60     | 8323       |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.56     | 16442      |
                | **Macro Avg**    | 0.56      | 0.56   | 0.56     | 16442      |
                | **Weighted Avg** | 0.56      | 0.56   | 0.56     | 16442      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/LOAN/LOAN_LogisticRegression_RUS.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying RUS resampling")#, use_container_width=True
            
        # ROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOS
            st.markdown('<h3 style="color: brown;">ROS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 13.35 %                 |
                | F1 Score                         | 59.51 %                 |
                | Accuracy Score                   | 56.59 %                 |
                | Recall Score                     | 63.94 %                 |
                | Precision Score                  | 55.66 %                 |
                | ROC AUC Score                    | 56.60 %                 |
                | False Positive Rate              | 50.73 %                 |
                | Negative Predictive Value        | 57.83 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 15192              | 15645              |
                | Positive         | 11077              | 19640              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.58      | 0.49   | 0.53     | 30837      |
                | 1                | 0.56      | 0.64   | 0.60     | 30717      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.57     | 61554      |
                | **Macro Avg**    | 0.57      | 0.57   | 0.56     | 61554      |
                | **Weighted Avg** | 0.57      | 0.57   | 0.56     | 61554      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/LOAN/LOAN_LogisticRegression_ROS.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying ROS resampling")#, use_container_width=True
            
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">SMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 14.24 %                 |
                | F1 Score                         | 60.99 %                 |
                | Accuracy Score                   | 56.94 %                 |
                | Recall Score                     | 67.46 %                 |
                | Precision Score                  | 55.66 %                 |
                | ROC AUC Score                    | 56.96 %                 |
                | False Positive Rate              | 53.54 %                 |
                | Negative Predictive Value        | 58.91 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 14327              | 16510              |
                | Positive         | 9994               | 20723              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.59      | 0.46   | 0.52     | 30837      |
                | 1                | 0.56      | 0.67   | 0.61     | 30717      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.57     | 61554      |
                | **Macro Avg**    | 0.57      | 0.57   | 0.56     | 61554      |
                | **Weighted Avg** | 0.57      | 0.57   | 0.56     | 61554      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/LOAN/LOAN_LogisticRegression_SMOTE.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying SMOTE resampling")#, use_container_width=True
            
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTEEEEEEEEEEEEENNNNNNNNNNNNNNNN
            st.markdown('<h3 style="color: brown;">SMOTEENN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)    
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 25.31 %                 |
                | F1 Score                         | 78.82 %                 |
                | Accuracy Score                   | 69.27 %                 |
                | Recall Score                     | 85.91 %                 |
                | Precision Score                  | 72.82 %                 |
                | ROC AUC Score                    | 61.00 %                 |
                | False Positive Rate              | 63.89 %                 |
                | Negative Predictive Value        | 56.27 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 4490               | 7945               |
                | Positive         | 3490               | 21283              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.56      | 0.36   | 0.44     | 12435      |
                | 1                | 0.73      | 0.86   | 0.79     | 24773      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.69     | 37208      |
                | **Macro Avg**    | 0.65      | 0.61   | 0.61     | 37208      |
                | **Weighted Avg** | 0.67      | 0.69   | 0.67     | 37208      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/LOAN/LOAN_LogisticRegression_SMOTEENN.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying SMOTEENN resampling")#, use_container_width=True
             
        # BBBBBBBBSMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">BSMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 15.40 %                 |
                | F1 Score                         | 60.69 %                 |
                | Accuracy Score                   | 57.58 %                 |
                | Recall Score                     | 65.61 %                 |
                | Precision Score                  | 56.45 %                 |
                | ROC AUC Score                    | 57.60 %                 |
                | False Positive Rate              | 50.41 %                 |
                | Negative Predictive Value        | 59.14 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 15291              | 15546              |
                | Positive         | 10563              | 20154              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.59      | 0.50   | 0.54     | 30837      |
                | 1                | 0.56      | 0.66   | 0.61     | 30717      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.58     | 61554      |
                | **Macro Avg**    | 0.58      | 0.58   | 0.57     | 61554      |
                | **Weighted Avg** | 0.58      | 0.58   | 0.57     | 61554      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/LOAN/LOAN_LogisticRegression_BSMOTE.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying BSMOTE resampling")#, use_container_width=True
                   
        # AaaaaaaaaaaaaaaaaaaaaaaaaDAaaaaaaaaaaaaaaaaaaaaaSsssssssssYyyyyNnnnn
            st.markdown('<h3 style="color: brown;">ADASYN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)           
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 12.64 %                 |
                | F1 Score                         | 61.30 %                 |
                | Accuracy Score                   | 56.30 %                 |
                | Recall Score                     | 68.24 %                 |
                | Precision Score                  | 55.63 %                 |
                | ROC AUC Score                    | 56.13 %                 |
                | False Positive Rate              | 55.98 %                 |
                | Negative Predictive Value        | 57.40 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 13501              | 17168              |
                | Positive         | 10020              | 21529              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.57      | 0.44   | 0.50     | 30669      |
                | 1                | 0.56      | 0.68   | 0.61     | 31549      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.56     | 62218      |
                | **Macro Avg**    | 0.57      | 0.56   | 0.56     | 62218      |
                | **Weighted Avg** | 0.57      | 0.56   | 0.56     | 62218      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/LOAN/LOAN_LogisticRegression_ADASYN.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying ADASYN resampling")#, use_container_width=True
            
        elif sidebar_option == "DT":
            # Display content for Option 1
            header()
            # Display text
            st.markdown('<h3 style="color: green;">Evaluation Metrics Using DecisionTreeClassifier and different resampling methods:</h3>', unsafe_allow_html=True)

        # RUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUS
            st.markdown('<h3 style="color: brown;">RUS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 08.82 %                 |
                | F1 Score                         | 54.72 %                 |
                | Accuracy Score                   | 54.41 %                 |
                | Recall Score                     | 54.43 %                 |
                | Precision Score                  | 55.02 %                 |
                | ROC AUC Score                    | 54.41 %                 |
                | False Positive Rate              | 45.61 %                 |
                | Negative Predictive Value        | 53.79 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 4416               | 3703               |
                | Positive         | 3793               | 4530               |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.54      | 0.54   | 0.54     | 8119       |
                | 1                | 0.55      | 0.54   | 0.55     | 8323       |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.54     | 16442      |
                | **Macro Avg**    | 0.54      | 0.54   | 0.54     | 16442      |
                | **Weighted Avg** | 0.54      | 0.54   | 0.54     | 16442      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/LOAN/LOAN_DecisionTreeClassifier_RUS.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying RUS resampling")#, use_container_width=True
            
        # ROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOS
            st.markdown('<h3 style="color: brown;">ROS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2) 
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 74.58 %                 |
                | F1 Score                         | 87.73 %                 |
                | Accuracy Score                   | 86.50 %                 |
                | Recall Score                     | 96.71 %                 |
                | Precision Score                  | 80.27 %                 |
                | ROC AUC Score                    | 86.52 %                 |
                | False Positive Rate              | 23.67 %                 |
                | Negative Predictive Value        | 95.88 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 23537              | 7300               |
                | Positive         | 1011               | 29706              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.96      | 0.76   | 0.85     | 30837      |
                | 1                | 0.80      | 0.97   | 0.88     | 30717      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.86     | 61554      |
                | **Macro Avg**    | 0.88      | 0.87   | 0.86     | 61554      |
                | **Weighted Avg** | 0.88      | 0.86   | 0.86     | 61554      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/LOAN/LOAN_DecisionTreeClassifier_ROS.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying ROS resampling")#, use_container_width=True
            
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">SMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 53.99 %                 |
                | F1 Score                         | 77.24 %                 |
                | Accuracy Score                   | 76.98 %                 |
                | Recall Score                     | 78.26 %                 |
                | Precision Score                  | 76.25 %                 |
                | ROC AUC Score                    | 76.99 %                 |
                | False Positive Rate              | 24.29 %                 |
                | Negative Predictive Value        | 77.76 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 23348              | 7489               |
                | Positive         | 6679               | 24038              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.78      | 0.76   | 0.77     | 30837      |
                | 1                | 0.76      | 0.78   | 0.77     | 30717      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.77     | 61554      |
                | **Macro Avg**    | 0.77      | 0.77   | 0.77     | 61554      |
                | **Weighted Avg** | 0.77      | 0.77   | 0.77     | 61554      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/LOAN/LOAN_DecisionTreeClassifier_SMOTE.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying SMOTE resampling")#, use_container_width=True
            
        
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTEEEEEEEEEEEEENNNNNNNNNNNNNNNN
            st.markdown('<h3 style="color: brown;">SMOTEENN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 53.70 %                 |
                | F1 Score                         | 84.81 %                 |
                | Accuracy Score                   | 79.58 %                 |
                | Recall Score                     | 85.64 %                 |
                | Precision Score                  | 84.01 %                 |
                | ROC AUC Score                    | 76.58 %                 |
                | False Positive Rate              | 32.48 %                 |
                | Negative Predictive Value        | 70.24 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 8396               | 4039               |
                | Positive         | 3558               | 21215              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.70      | 0.68   | 0.69     | 12435      |
                | 1                | 0.84      | 0.86   | 0.85     | 24773      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.80     | 37208      |
                | **Macro Avg**    | 0.77      | 0.77   | 0.77     | 37208      |
                | **Weighted Avg** | 0.79      | 0.80   | 0.79     | 37208      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/LOAN/LOAN_DecisionTreeClassifier_SMOTEENN.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying SMOTEENN resampling")#, use_container_width=True
         
        # BBBBBBBBSMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">BSMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 53.63 %                 |
                | F1 Score                         | 77.10 %                 |
                | Accuracy Score                   | 76.80 %                 |
                | Recall Score                     | 78.27 %                 |
                | Precision Score                  | 75.97 %                 |
                | ROC AUC Score                    | 76.81 %                 |
                | False Positive Rate              | 24.66 %                 |
                | Negative Predictive Value        | 77.67 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 23234              | 7603               |
                | Positive         | 6676               | 24041              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.78      | 0.75   | 0.76     | 30837      |
                | 1                | 0.76      | 0.78   | 0.77     | 30717      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.77     | 61554      |
                | **Macro Avg**    | 0.77      | 0.77   | 0.77     | 61554      |
                | **Weighted Avg** | 0.77      | 0.77   | 0.77     | 61554      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/LOAN/LOAN_DecisionTreeClassifier_BSMOTE.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying BSMOTE resampling")#, use_container_width=True
            
         
        # AaaaaaaaaaaaaaaaaaaaaaaaaDAaaaaaaaaaaaaaaaaaaaaaSsssssssssYyyyyNnnnn
            st.markdown('<h3 style="color: brown;">ADASYN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 54.20 %                 |
                | F1 Score                         | 77.71 %                 |
                | Accuracy Score                   | 77.10 %                 |
                | Recall Score                     | 78.70 %                 |
                | Precision Score                  | 76.74 %                 |
                | ROC AUC Score                    | 77.08 %                 |
                | False Positive Rate              | 24.54 %                 |
                | Negative Predictive Value        | 77.50 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 23143              | 7526               |
                | Positive         | 6721               | 24828              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.77      | 0.75   | 0.76     | 30669      |
                | 1                | 0.77      | 0.79   | 0.78     | 31549      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.77     | 62218      |
                | **Macro Avg**    | 0.77      | 0.77   | 0.77     | 62218      |
                | **Weighted Avg** | 0.77      | 0.77   | 0.77     | 62218      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/LOAN/LOAN_DecisionTreeClassifier_ADASYN.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying ADASYN resampling")#, use_container_width=True

        elif sidebar_option == "RF":
            # Display content for Option 1
            header()
            # Display text
            st.markdown('<h3 style="color: green;">Evaluation Metrics Using RandomForestClassifier and different resampling methods:</h3>', unsafe_allow_html=True)

        # RUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUS
            st.markdown('<h3 style="color: brown;">RUS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 22.20 %                 |
                | F1 Score                         | 61.18 %                 |
                | Accuracy Score                   | 61.09 %                 |
                | Recall Score                     | 60.57 %                 |
                | Precision Score                  | 61.81 %                 |
                | ROC AUC Score                    | 61.10 %                 |
                | False Positive Rate              | 38.37 %                 |
                | Negative Predictive Value        | 60.39 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 5004               | 3115               |
                | Positive         | 3282               | 5041               |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.60      | 0.62   | 0.61     | 8119       |
                | 1                | 0.62      | 0.61   | 0.61     | 8323       |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.61     | 16442      |
                | **Macro Avg**    | 0.61      | 0.61   | 0.61     | 16442      |
                | **Weighted Avg** | 0.61      | 0.61   | 0.61     | 16442      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/LOAN/LOAN_RandomForestClassifier_RUS.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying RUS resampling")#, use_container_width=True
            
        # ROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOS
            st.markdown('<h3 style="color: brown;">ROS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 89.69 %                 |
                | F1 Score                         | 94.88 %                 |
                | Accuracy Score                   | 94.84 %                 |
                | Recall Score                     | 95.94 %                 |
                | Precision Score                  | 93.84 %                 |
                | ROC AUC Score                    | 94.84 %                 |
                | False Positive Rate              | 06.27 %                 |
                | Negative Predictive Value        | 95.87 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 28904              | 1933               |
                | Positive         | 1246               | 29471              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.96      | 0.94   | 0.95     | 30837      |
                | 1                | 0.94      | 0.96   | 0.95     | 30717      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.95     | 61554      |
                | **Macro Avg**    | 0.95      | 0.95   | 0.95     | 61554      |
                | **Weighted Avg** | 0.95      | 0.95   | 0.95     | 61554      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/LOAN/LOAN_RandomForestClassifier_ROS.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying ROS resampling")#, use_container_width=True
            
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">SMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 72.88 %                 |
                | F1 Score                         | 84.50 %                 |
                | Accuracy Score                   | 85.88 %                 |
                | Recall Score                     | 77.09 %                 |
                | Precision Score                  | 93.47 %                 |
                | ROC AUC Score                    | 85.87 %                 |
                | False Positive Rate              | 05.36 %                 |
                | Negative Predictive Value        | 80.57 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 29183              | 1654               |
                | Positive         | 7036               | 23681              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.81      | 0.95   | 0.87     | 30837      |
                | 1                | 0.93      | 0.77   | 0.84     | 30717      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.86     | 61554      |
                | **Macro Avg**    | 0.87      | 0.86   | 0.86     | 61554      |
                | **Weighted Avg** | 0.87      | 0.86   | 0.86     | 61554      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/LOAN/LOAN_RandomForestClassifier_SMOTE.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying SMOTE resampling")#, use_container_width=True
            
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTEEEEEEEEEEEEENNNNNNNNNNNNNNNN
            st.markdown('<h3 style="color: brown;">SMOTEENN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 70.53 %                 |
                | F1 Score                         | 90.41 %                 |
                | Accuracy Score                   | 87.05 %                 |
                | Recall Score                     | 91.72 %                 |
                | Precision Score                  | 89.13 %                 |
                | ROC AUC Score                    | 84.72 %                 |
                | False Positive Rate              | 22.28 %                 |
                | Negative Predictive Value        | 82.50 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 9665               | 2770               |
                | Positive         | 2050               | 22723              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.83      | 0.78   | 0.80     | 12435      |
                | 1                | 0.89      | 0.92   | 0.90     | 24773      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.87     | 37208      |
                | **Macro Avg**    | 0.86      | 0.85   | 0.85     | 37208      |
                | **Weighted Avg** | 0.87      | 0.87   | 0.87     | 37208      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/LOAN/LOAN_RandomForestClassifier_SMOTEENN.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying SMOTEENN resampling")#, use_container_width=True
    
        # BBBBBBBBSMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">BSMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 73.00 %                 |
                | F1 Score                         | 84.60 %                 |
                | Accuracy Score                   | 85.96 %                 |
                | Recall Score                     | 77.30 %                 |
                | Precision Score                  | 93.43 %                 |
                | ROC AUC Score                    | 85.94 %                 |
                | False Positive Rate              | 05.42 %                 |
                | Negative Predictive Value        | 80.71 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 29167              | 1670               |
                | Positive         | 6973               | 23744              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.81      | 0.95   | 0.87     | 30837      |
                | 1                | 0.93      | 0.77   | 0.85     | 30717      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.86     | 61554      |
                | **Macro Avg**    | 0.87      | 0.86   | 0.86     | 61554      |
                | **Weighted Avg** | 0.87      | 0.86   | 0.86     | 61554      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/LOAN/LOAN_RandomForestClassifier_BSMOTE.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying BSMOTE resampling")#, use_container_width=True
            
           
        # AaaaaaaaaaaaaaaaaaaaaaaaaDAaaaaaaaaaaaaaaaaaaaaaSsssssssssYyyyyNnnnn
            st.markdown('<h3 style="color: brown;">ADASYN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)           
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 72.98 %                 |
                | F1 Score                         | 84.81 %                 |
                | Accuracy Score                   | 85.91 %                 |
                | Recall Score                     | 77.56 %                 |
                | Precision Score                  | 93.55 %                 |
                | ROC AUC Score                    | 86.03 %                 |
                | False Positive Rate              | 05.50 %                 |
                | Negative Predictive Value        | 80.37 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 28981              | 1688               |
                | Positive         | 7079               | 24470              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.80      | 0.94   | 0.87     | 30669      |
                | 1                | 0.94      | 0.78   | 0.85     | 31549      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.86     | 62218      |
                | **Macro Avg**    | 0.87      | 0.86   | 0.86     | 62218      |
                | **Weighted Avg** | 0.87      | 0.86   | 0.86     | 62218      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/LOAN/LOAN_RandomForestClassifier_ADASYN.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying ADASYN resampling")#, use_container_width=True
            
        elif sidebar_option == "XGB":
            # Display content for Option 2
            header()                       
            # Display text
            st.markdown('<h3 style="color: green;">Evaluation Metrics Using XGBClassifier and different resampling methods:</h3>', unsafe_allow_html=True)

        # RUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUS
            st.markdown('<h3 style="color: brown;">RUS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 23.24 %                 |
                | F1 Score                         | 62.52 %                 |
                | Accuracy Score                   | 61.63 %                 |
                | Recall Score                     | 63.21 %                 |
                | Precision Score                  | 61.84 %                 |
                | ROC AUC Score                    | 61.62 %                 |
                | False Positive Rate              | 39.98 %                 |
                | Negative Predictive Value        | 61.41 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 4873               | 3246               |
                | Positive         | 3062               | 5261               |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.61      | 0.60   | 0.61     | 8119       |
                | 1                | 0.62      | 0.63   | 0.63     | 8323       |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.62     | 16442      |
                | **Macro Avg**    | 0.62      | 0.62   | 0.62     | 16442      |
                | **Weighted Avg** | 0.62      | 0.62   | 0.62     | 16442      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/LOAN/LOAN_XGBClassifier_RUS.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying RUS resampling")#, use_container_width=True
            

        # ROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOS
            st.markdown('<h3 style="color: brown;">ROS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)          
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 35.04 %                 |
                | F1 Score                         | 68.62 %                 |
                | Accuracy Score                   | 67.46 %                 |
                | Recall Score                     | 71.29 %                 |
                | Precision Score                  | 66.14 %                 |
                | ROC AUC Score                    | 67.47 %                 |
                | False Positive Rate              | 36.35 %                 |
                | Negative Predictive Value        | 68.99 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 19628              | 11209              |
                | Positive         | 8820               | 21897              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.69      | 0.64   | 0.66     | 30837      |
                | 1                | 0.66      | 0.71   | 0.69     | 30717      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.67     | 61554      |
                | **Macro Avg**    | 0.68      | 0.67   | 0.67     | 61554      |
                | **Weighted Avg** | 0.68      | 0.67   | 0.67     | 61554      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/LOAN/LOAN_XGBClassifier_ROS.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying ROS resampling")#, use_container_width=True
            

        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">SMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)        
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 70.78 %                 |
                | F1 Score                         | 82.52 %                 |
                | Accuracy Score                   | 84.50 %                 |
                | Recall Score                     | 73.29 %                 |
                | Precision Score                  | 94.41 %                 |
                | ROC AUC Score                    | 84.48 %                 |
                | False Positive Rate              | 04.33 %                 |
                | Negative Predictive Value        | 78.24 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 29503              | 1334               |
                | Positive         | 8204               | 22513              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.78      | 0.96   | 0.86     | 30837      |
                | 1                | 0.94      | 0.73   | 0.83     | 30717      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.85     | 61554      |
                | **Macro Avg**    | 0.86      | 0.84   | 0.84     | 61554      |
                | **Weighted Avg** | 0.86      | 0.85   | 0.84     | 61554      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/LOAN/LOAN_XGBClassifier_SMOTE.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying SMOTE resampling")#, use_container_width=True
            
        
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTEEEEEEEEEEEEENNNNNNNNNNNNNNNN
            st.markdown('<h3 style="color: brown;">SMOTEENN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 68.87 %                 |
                | F1 Score                         | 89.21 %                 |
                | Accuracy Score                   | 85.87 %                 |
                | Recall Score                     | 87.69 %                 |
                | Precision Score                  | 90.78 %                 |
                | ROC AUC Score                    | 84.97 %                 |
                | False Positive Rate              | 17.74 %                 |
                | Negative Predictive Value        | 77.03 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 10229              | 2206               |
                | Positive         | 3050               | 21723              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.77      | 0.82   | 0.80     | 12435      |
                | 1                | 0.91      | 0.88   | 0.89     | 24773      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.86     | 37208      |
                | **Macro Avg**    | 0.84      | 0.85   | 0.84     | 37208      |
                | **Weighted Avg** | 0.86      | 0.86   | 0.86     | 37208      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/LOAN/LOAN_XGBClassifier_SMOTEENN.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying SMOTEENN resampling")#, use_container_width=True
                      
        # BBBBBBBBSMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">BSMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 70.73 %                 |
                | F1 Score                         | 82.42 %                 |
                | Accuracy Score                   | 84.45 %                 |
                | Recall Score                     | 73.05 %                 |
                | Precision Score                  | 94.54 %                 |
                | ROC AUC Score                    | 84.42 %                 |
                | False Positive Rate              | 04.20 %                 |
                | Negative Predictive Value        | 78.11 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 29542              | 1295               |
                | Positive         | 8279               | 22438              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.78      | 0.96   | 0.86     | 30837      |
                | 1                | 0.95      | 0.73   | 0.82     | 30717      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.84     | 61554      |
                | **Macro Avg**    | 0.86      | 0.84   | 0.84     | 61554      |
                | **Weighted Avg** | 0.86      | 0.84   | 0.84     | 61554      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/LOAN/LOAN_XGBClassifier_BSMOTE.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying BSMOTE resampling")#, use_container_width=True
                
        # AaaaaaaaaaaaaaaaaaaaaaaaaDAaaaaaaaaaaaaaaaaaaaaaSsssssssssYyyyyNnnnn
            st.markdown('<h3 style="color: brown;">ADASYN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2) 
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 71.58 %                 |
                | F1 Score                         | 83.00 %                 |
                | Accuracy Score                   | 84.76 %                 |
                | Recall Score                     | 73.42 %                 |
                | Precision Score                  | 95.47 %                 |
                | ROC AUC Score                    | 84.92 %                 |
                | False Positive Rate              | 03.58 %                 |
                | Negative Predictive Value        | 77.91 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 29570              | 1099               |
                | Positive         | 8386               | 23163              |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.78      | 0.96   | 0.86     | 30669      |
                | 1                | 0.95      | 0.73   | 0.83     | 31549      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.85     | 62218      |
                | **Macro Avg**    | 0.87      | 0.85   | 0.85     | 62218      |
                | **Weighted Avg** | 0.87      | 0.85   | 0.85     | 62218      |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/LOAN/LOAN_XGBClassifier_ADASYN.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying ADASYN resampling")#, use_container_width=True
    
    def Info_NSD():
        if sidebar_option == "Methodology":
            Methodology()
        
        elif sidebar_option =='Dataset info':
            header()
            st.write('## NSD Dataset')
            st.write("""

            NSD Dataset (Simulated) 

            This is a simulated credit card transaction dataset containing legitimate and fraudulent transactions for the period 1ᵉʳ January 2019 to 31 December 2020.  It covers the credit cards of 1000 customers transacting with a pool of 800 merchants over 6 months. over a period of 6 months. they used training and test segments directly from the source and a randomly sampled test segment.

            The dataset was generated using the Sparkov data generation tool and they modified a version of the dataset created for Kaggle.
                     
            - Source license: https://creativecommons.org/publicdomain/zero/1.0/
                     
            - Variables: `Transaction date, credit card number, merchant, category, amount, name, street, gender etc`. 
                     
            - All variables are synthetically generated using the [Sparkov](https://www.kaggle.com/datasets/kartik2112/fraud-detection) tool
                     
            - Fraud category: Card Not Present Transaction Fraud
                     
            - Provider: Kartik Shenoy
                     
            - Release date: 2020-08-05
            

            Link to dataset: [See here](https://www.kaggle.com/kartik2112/fraud-detection) 
                         """)
                      
        elif sidebar_option == "LR":
            # # Display content for Option 1
            header()
            # Display text
            st.markdown('<h3 style="color: green;">Evaluation Metrics Using LogisticRegression and different resampling methods:</h3>', unsafe_allow_html=True)

        # RUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUS
            st.markdown('<h3 style="color: brown;">RUS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)  
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 00.00 %                 |
                | F1 Score                         | 00.00 %                 |
                | Accuracy Score                   | 50.35 %                 |
                | Recall Score                     | 00.00 %                 |
                | Precision Score                  | 00.00 %                 |
                | ROC AUC Score                    | 50.00 %                 |Figs/
                | False Positive Rate              | 00.00 %                 |
                | Negative Predictive Value        | 50.35 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 1870               | 0                  |
                | Positive         | 1844               | 0                  |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.50      | 1.00   | 0.67     | 1870       |
                | 1                | 0.00      | 0.00   | 0.00     | 1844       |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.50     | 3714       |
                | **Macro Avg**    | 0.25      | 0.50   | 0.33     | 3714       |
                | **Weighted Avg** | 0.25      | 0.50   | 0.34     | 3714       |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/NSD/NSD_LogisticRegression_RUS.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying RUS resampling")#, use_container_width=True
            
        # ROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOS
            st.markdown('<h3 style="color: brown;">ROS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 00.00 %                 |
                | F1 Score                         | 00.00 %                 |
                | Accuracy Score                   | 49.91 %                 |
                | Recall Score                     | 00.00 %                 |
                | Precision Score                  | 00.00 %                 |
                | ROC AUC Score                    | 50.00 %                 |
                | False Positive Rate              | 00.00 %                 |
                | Negative Predictive Value        | 49.91 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 355992             | 0                  |
                | Positive         | 357264             | 0                  |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.50      | 1.00   | 0.67     | 355992     |
                | 1                | 0.00      | 0.00   | 0.00     | 357264     |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.50     | 713256     |
                | **Macro Avg**    | 0.25      | 0.50   | 0.33     | 713256     |
                | **Weighted Avg** | 0.25      | 0.50   | 0.33     | 713256     |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/NSD/NSD_LogisticRegression_ROS.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying ROS resampling")#, use_container_width=True
            
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">SMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 00.00 %                 |
                | F1 Score                         | 00.00 %                 |
                | Accuracy Score                   | 49.91 %                 |
                | Recall Score                     | 00.00 %                 |
                | Precision Score                  | 00.00 %                 |
                | ROC AUC Score                    | 50.00 %                 |
                | False Positive Rate              | 00.00 %                 |
                | Negative Predictive Value        | 49.91 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 355992             | 0                  |
                | Positive         | 357264             | 0                  |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.50      | 1.00   | 0.67     | 355992     |
                | 1                | 0.00      | 0.00   | 0.00     | 357264     |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.50     | 713256     |
                | **Macro Avg**    | 0.25      | 0.50   | 0.33     | 713256     |
                | **Weighted Avg** | 0.25      | 0.50   | 0.33     | 713256     |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/NSD/NSD_LogisticRegression_SMOTE.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying SMOTE resampling")#, use_container_width=True
            
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTEEEEEEEEEEEEENNNNNNNNNNNNNNNN
            st.markdown('<h3 style="color: brown;">SMOTEENN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)    
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performance Metrics")
                st.markdown("""
                | Metric                           | Score                    |
                |----------------------------------|--------------------------|
                | Matthews Correlation Coefficient | 00.00 %                  |
                | F1 Score                         | 00.00 %                  |
                | Accuracy Score                   | 78.72 %                  |
                | Recall Score                     | 00.00 %                  |
                | Precision Score                  | 00.00 %                  |
                | ROC AUC Score                    | 50.00 %                  |
                | False Positive Rate              | 00.00 %                  |
                | Negative Predictive Value        | 78.72 %                  |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 355153             | 0                  |
                | Positive         | 96024              | 0                  |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support   |
                |------------------|-----------|--------|----------|-----------|
                | 0                | 0.79      | 1.00   | 0.88     | 355153    |
                | 1                | 0.00      | 0.00   | 0.00     | 96024     |
                |                  |           |        |          |           |
                | **Accuracy**     |           |        | 0.79     | 451177    |
                | **Macro Avg**    | 0.39      | 0.50   | 0.44     | 451177    |
                | **Weighted Avg** | 0.62      | 0.79   | 0.69     | 451177    |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/NSD/NSD_LogisticRegression_SMOTEENN.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying SMOTEENN resampling")#, use_container_width=True
             
        # BBBBBBBBSMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">BSMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performance Metrics")
                st.markdown(f"""
                | Metric                           | Score                   |
                |----------------------------------|-------------------------|
                | Matthews Correlation Coefficient | 00.00 %                 |
                | F1 Score                         | 00.00 %                 |
                | Accuracy Score                   | 49.91 %                 |
                | Recall Score                     | 00.00 %                 |
                | Precision Score                  | 00.00 %                 |
                | ROC AUC Score                    | 50.00 %                 |
                | False Positive Rate              | 00.00 %                 |
                | Negative Predictive Value        | 49.91 %                 |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 355992             | 0                  |
                | Positive         | 357264             | 0                  |
                """)
            # Table 2: Classification Report
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.50      | 1.00   | 0.67     | 355992     |
                | 1                | 0.00      | 0.00   | 0.00     | 357264     |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.50     | 713256     |
                | **Macro Avg**    | 0.25      | 0.50   | 0.33     | 713256     |
                | **Weighted Avg** | 0.25      | 0.50   | 0.33     | 713256     |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/NSD/NSD_LogisticRegression_BSMOTE.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying BSMOTE resampling")#, use_container_width=True
                   
        # AaaaaaaaaaaaaaaaaaaaaaaaaDAaaaaaaaaaaaaaaaaaaaaaSsssssssssYyyyyNnnnn
            st.markdown('<h3 style="color: brown;">ADASYN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)           
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performance Metrics")
                st.markdown(f"""
                | Metric                           | Score                    |
                |----------------------------------|--------------------------|
                | Matthews Correlation Coefficient | 00.00 %                  |
                | F1 Score                         | 66.76 %                  |
                | Accuracy Score                   | 50.10 %                  |
                | Recall Score                     | 100.0 %                  |
                | Precision Score                  | 50.10 %                  |
                | ROC AUC Score                    | 50.00 %                  |
                | False Positive Rate              | 100.0 %                  |
                | Negative Predictive Value        | NaN                      |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                | Actual / Predicted |  Negative |  Positive |
                |-------------------|-----------|------------|
                | Negative          | 0         | 356202     |
                | Positive          | 0         | 356427     |
                """)
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.00      | 0.00   | 0.00     | 356202     |
                | 1                | 0.50      | 1.00   | 0.67     | 356427     |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.50     | 712629     |
                | **Macro Avg**    | 0.25      | 0.50   | 0.33     | 712629     |
                | **Weighted Avg** | 0.25      | 0.50   | 0.33     | 712629     |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/NSD/NSD_LogisticRegression_ADASYN.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying ADASYN resampling")#, use_container_width=True
            
        elif sidebar_option == "DT":
            # Display content for Option 1
            header()
            # Display text
            st.markdown('<h3 style="color: green;">Evaluation Metrics Using DecisionTreeClassifier and different resampling methods:</h3>', unsafe_allow_html=True)

        # RUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUS
            st.markdown('<h3 style="color: brown;">RUS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 90.47 %                   |
                | F1 Score                         | 95.21 %                   |
                | Accuracy Score                   | 95.23 %                   |
                | Recall Score                     | 95.50 %                   |
                | Precision Score                  | 94.93 %                   |
                | ROC AUC Score                    | 95.24 %                   |
                | False Positive Rate              | 05.03 %                   |
                | Negative Predictive Value        | 95.54 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 1776               | 94                 |
                | Positive         | 83                 | 1761               |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.96      | 0.95   | 0.95     | 1870       |
                | 1                | 0.95      | 0.95   | 0.95     | 1844       |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.95     | 3714       |
                | **Macro Avg**    | 0.95      | 0.95   | 0.95     | 3714       |
                | **Weighted Avg** | 0.95      | 0.95   | 0.95     | 3714       |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/NSD/NSD_DecisionTreeClassifier_RUS.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying RUS resampling")#, use_container_width=True
            
        # ROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOS
            st.markdown('<h3 style="color: brown;">ROS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2) 
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 99.82 %                   |
                | F1 Score                         | 99.91 %                   |
                | Accuracy Score                   | 99.91 %                   |
                | Recall Score                     | 100.0 %                   |
                | Precision Score                  | 99.82 %                   |
                | ROC AUC Score                    | 99.91 %                   |
                | False Positive Rate              | 00.18 %                   |
                | Negative Predictive Value        | 100.0 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 355338             | 654                |
                | Positive         | 0                  | 357264             |
                """) 
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 355992     |
                | 1                | 1.00      | 1.00   | 1.00     | 357264     |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 713256     |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 713256     |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 713256     |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/NSD/NSD_DecisionTreeClassifier_ROS.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying ROS resampling")#, use_container_width=True
            
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">SMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 97.31 %                   |
                | F1 Score                         | 98.66 %                   |
                | Accuracy Score                   | 98.65 %                   |
                | Recall Score                     | 99.27 %                   |
                | Precision Score                  | 98.06 %                   |
                | ROC AUC Score                    | 98.65 %                   |
                | False Positive Rate              | 01.97 %                   |
                | Negative Predictive Value        | 99.26 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 348993             | 6999               |
                | Positive         | 2613               | 354651             |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.99      | 0.98   | 0.99     | 355992     |
                | 1                | 0.98      | 0.99   | 0.99     | 357264     |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.99     | 713256     |
                | **Macro Avg**    | 0.99      | 0.99   | 0.99     | 713256     |
                | **Weighted Avg** | 0.99      | 0.99   | 0.99     | 713256     |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/NSD/NSD_DecisionTreeClassifier_SMOTE.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying SMOTE resampling")#, use_container_width=True
                
            
            # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTEEEEEEEEEEEEENNNNNNNNNNNNNNNN
            st.markdown('<h3 style="color: brown;">SMOTEENN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performance Metrics")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 99.03 %                   |
                | F1 Score                         | 99.24 %                   |
                | Accuracy Score                   | 99.67 %                   |
                | Recall Score                     | 99.56 %                   |
                | Precision Score                  | 98.91 %                   |
                | ROC AUC Score                    | 99.63 %                   |
                | False Positive Rate              | 00.30 %                   |
                | Negative Predictive Value        | 99.88 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 354098             | 1055               |
                | Positive         | 419                | 95605              |
                """)   
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 355153     |
                | 1                | 0.99      | 1.00   | 0.99     | 96024      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 451177     |
                | **Macro Avg**    | 0.99      | 1.00   | 1.00     | 451177     |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 451177     |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/NSD/NSD_DecisionTreeClassifier_SMOTEENN.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying SMOTEENN resampling")#, use_container_width=True
            
        # BBBBBBBBSMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">BSMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 99.40 %                   |
                | F1 Score                         | 99.70 %                   |
                | Accuracy Score                   | 99.70 %                   |
                | Recall Score                     | 99.83 %                   |
                | Precision Score                  | 99.57 %                   |
                | ROC AUC Score                    | 99.70 %                   |
                | False Positive Rate              | 00.04 %                   |
                | Negative Predictive Value        | 99.83 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 354446             | 1546               |
                | Positive         | 606                | 356658             |
                """)                
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 355992     |
                | 1                | 1.00      | 1.00   | 1.00     | 357264     |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 713256     |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 713256     |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 713256     |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/NSD/NSD_DecisionTreeClassifier_BSMOTE.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying BSMOTE resampling")#, use_container_width=True
            
        
        # AaaaaaaaaaaaaaaaaaaaaaaaaDAaaaaaaaaaaaaaaaaaaaaaSsssssssssYyyyyNnnnn
            st.markdown('<h3 style="color: brown;">ADASYN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 97.48 %                   |
                | F1 Score                         | 98.75 %                   |
                | Accuracy Score                   | 98.74 %                   |
                | Recall Score                     | 99.37 %                   |
                | Precision Score                  | 98.13 %                   |
                | ROC AUC Score                    | 98.73 %                   |
                | False Positive Rate              | 01.90 %                   |
                | Negative Predictive Value        | 99.36 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 349227             | 6757               |
                | Positive         | 2256               | 355214             |
                """)                
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.99      | 0.98   | 0.99     | 355984     |
                | 1                | 0.98      | 0.99   | 0.99     | 357470     |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.99     | 713454     |
                | **Macro Avg**    | 0.99      | 0.99   | 0.99     | 713454     |
                | **Weighted Avg** | 0.99      | 0.99   | 0.99     | 713454     |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/NSD/NSD_DecisionTreeClassifier_ADASYN.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying ADASYN resampling")#, use_container_width=True

        elif sidebar_option == "RF":
            # Display content for Option 1
            header()
            # Display text
            st.markdown('<h3 style="color: green;">Evaluation Metrics Using RandomForestClassifier and different resampling methods:</h3>', unsafe_allow_html=True)

        # RUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUS
            st.markdown('<h3 style="color: brown;">RUS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 90.94 %                   |
                | F1 Score                         | 95.34 %                   |
                | Accuracy Score                   | 95.45 %                   |
                | Recall Score                     | 93.82 %                   |
                | Precision Score                  | 96.92 %                   |
                | ROC AUC Score                    | 95.44 %                   |
                | False Positive Rate              | 02.94 %                   |
                | Negative Predictive Value        | 94.09 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 1815               | 55                 |
                | Positive         | 114                | 1730               |
                """)  
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.94      | 0.97   | 0.96     | 1870       |
                | 1                | 0.97      | 0.94   | 0.95     | 1844       |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.95     | 3714       |
                | **Macro Avg**    | 0.96      | 0.95   | 0.95     | 3714       |
                | **Weighted Avg** | 0.95      | 0.95   | 0.95     | 3714       |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/NSD/NSD_RandomForestClassifier_RUS.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying RUS resampling")#, use_container_width=True
            
        # ROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOS
            st.markdown('<h3 style="color: brown;">ROS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 99.96 %                   |
                | F1 Score                         | 99.98 %                   |
                | Accuracy Score                   | 99.98 %                   |
                | Recall Score                     | 100.0 %                   |
                | Precision Score                  | 99.96 %                   |
                | ROC AUC Score                    | 99.98 %                   |
                | False Positive Rate              | 00.04 %                   |
                | Negative Predictive Value        | 100.0 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 355840             | 152                |
                | Positive         | 0                  | 357264             |
                """) 
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 355992     |
                | 1                | 1.00      | 1.00   | 1.00     | 357264     |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 713256     |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 713256     |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 713256     |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/NSD/NSD_RandomForestClassifier_ROS.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying ROS resampling")#, use_container_width=True
            
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">SMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 99.68 %                   |
                | F1 Score                         | 99.84 %                   |
                | Accuracy Score                   | 99.84 %                   |
                | Recall Score                     | 99.98 %                   |
                | Precision Score                  | 99.70 %                   |
                | ROC AUC Score                    | 99.84 %                   |
                | False Positive Rate              | 00.30 %                   |
                | Negative Predictive Value        | 99.98 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 354921             | 1071               |
                | Positive         | 65                 | 357199             |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 355992     |
                | 1                | 1.00      | 1.00   | 1.00     | 357264     |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 713256     |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 713256     |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 713256     |
                """)
                        # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/NSD/NSD_RandomForestClassifier_SMOTE.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying SMOTE resampling")#, use_container_width=True
            
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTEEEEEEEEEEEEENNNNNNNNNNNNNNNN
            st.markdown('<h3 style="color: brown;">SMOTEENN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performance Metrics")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 99.91 %                   |
                | F1 Score                         | 99.93 %                   |
                | Accuracy Score                   | 99.97 %                   |
                | Recall Score                     | 99.95 %                   |
                | Precision Score                  | 99.92 %                   |
                | ROC AUC Score                    | 99.96 %                   |
                | False Positive Rate              | 00.02 %                   |
                | Negative Predictive Value        | 99.99 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 355074             | 79                 |
                | Positive         | 52                 | 95972              |
                """) 
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 355153     |
                | 1                | 1.00      | 1.00   | 1.00     | 96024      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 451177     |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 451177     |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 451177     |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/NSD/NSD_RandomForestClassifier_SMOTEENN.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying SMOTEENN resampling")#, use_container_width=True
    
        # BBBBBBBBSMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">BSMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performance Metrics")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 99.80 %                   |
                | F1 Score                         | 99.90 %                   |
                | Accuracy Score                   | 99.90 %                   |
                | Recall Score                     | 99.85 %                   |
                | Precision Score                  | 99.94 %                   |
                | ROC AUC Score                    | 99.90 %                   |
                | False Positive Rate              | 00.06 %                   |
                | Negative Predictive Value        | 99.85 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 355788             | 204                |
                | Positive         | 526                | 356738             |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 355992     |
                | 1                | 1.00      | 1.00   | 1.00     | 357264     |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.99     | 713256     |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 713256     |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 713256     |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/NSD/NSD_RandomForestClassifier_BSMOTE.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying BSMOTE resampling")#, use_container_width=True
            
           
        # AaaaaaaaaaaaaaaaaaaaaaaaaDAaaaaaaaaaaaaaaaaaaaaaSsssssssssYyyyyNnnnn
            st.markdown('<h3 style="color: brown;">ADASYN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)           
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performance Metrics")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 99.69 %                   |
                | F1 Score                         | 99.84 %                   |
                | Accuracy Score                   | 99.84 %                   |
                | Recall Score                     | 99.97 %                   |
                | Precision Score                  | 99.72 %                   |
                | ROC AUC Score                    | 99.84 %                   |
                | False Positive Rate              | 00.28 %                   |
                | Negative Predictive Value        | 99.97 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 355218             | 984                |
                | Positive         | 123                | 356304             |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 356202     |
                | 1                | 1.00      | 1.00   | 1.00     | 356427     |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 712629     |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 712629     |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 712629     |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/NSD/NSD_RandomForestClassifier_ADASYN.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying ADASYN resampling")#, use_container_width=True
            
        elif sidebar_option == "XGB":
            # Display content for Option 2
            header()                       
            # Display text
            st.markdown('<h3 style="color: green;">Evaluation Metrics Using XGBClassifier and different resampling methods:</h3>', unsafe_allow_html=True)

        # RUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUS
            st.markdown('<h3 style="color: brown;">RUS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 93.43 %                   |
                | F1 Score                         | 96.71 %                   |
                | Accuracy Score                   | 96.72 %                   |
                | Recall Score                     | 97.18 %                   |
                | Precision Score                  | 96.24 %                   |
                | ROC AUC Score                    | 96.72 %                   |
                | False Positive Rate              | 03.74 %                   |
                | Negative Predictive Value        | 97.19 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 1800               | 70                 |
                | Positive         | 52                 | 1792               |
                """)               
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.97      | 0.96   | 0.97     | 1870       |
                | 1                | 0.96      | 0.97   | 0.97     | 1844       |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.97     | 3714       |
                | **Macro Avg**    | 0.97      | 0.97   | 0.97     | 3714       |
                | **Weighted Avg** | 0.97      | 0.97   | 0.97     | 3714       |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/NSD/NSD_XGBClassifier_RUS.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying RUS resampling")#, use_container_width=True
            
        # ROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOS
            st.markdown('<h3 style="color: brown;">ROS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)          
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 98.91 %                   |
                | F1 Score                         | 99.46 %                   |
                | Accuracy Score                   | 99.45 %                   |
                | Recall Score                     | 100.0 %                   |
                | Precision Score                  | 98.92 %                   |
                | ROC AUC Score                    | 99.45 %                   |
                | False Positive Rate              | 01.10 %                   |
                | Negative Predictive Value        | 100.0 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 352077             | 3915               |
                | Positive         | 0                  | 357264             |
                """)   
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 0.99   | 0.99     | 355992     |
                | 1                | 0.99      | 1.00   | 0.99     | 357264     |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.99     | 713256     |
                | **Macro Avg**    | 0.99      | 1.00   | 0.99     | 713256     |
                | **Weighted Avg** | 0.99      | 0.99   | 0.99     | 713256     |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/NSD/NSD_XGBClassifier_ROS.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying ROS resampling")#, use_container_width=True
            

        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">SMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)        
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 95.39 %                   |
                | F1 Score                         | 97.67 %                   |
                | Accuracy Score                   | 97.69 %                   |
                | Recall Score                     | 96.85 %                   |
                | Precision Score                  | 98.51 %                   |
                | ROC AUC Score                    | 97.69 %                   |
                | False Positive Rate              | 01.47 %                   |
                | Negative Predictive Value        | 96.89 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 350770             | 5222               |
                | Positive         | 11271              | 345993             |
                """) 
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.97      | 0.99   | 0.98     | 355992     |
                | 1                | 0.99      | 0.97   | 0.98     | 357264     |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.98     | 713256     |
                | **Macro Avg**    | 0.98      | 0.98   | 0.98     | 713256     |
                | **Weighted Avg** | 0.98      | 0.98   | 0.98     | 713256     |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/NSD/NSD_XGBClassifier_SMOTE.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying SMOTE resampling")#, use_container_width=True
            
        
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTEEEEEEEEEEEEENNNNNNNNNNNNNNNN
            st.markdown('<h3 style="color: brown;">SMOTEENN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performance Metrics")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 99.15 %                   |
                | F1 Score                         | 99.33 %                   |
                | Accuracy Score                   | 99.72 %                   |
                | Recall Score                     | 99.23 %                   |
                | Precision Score                  | 99.43 %                   |
                | ROC AUC Score                    | 99.54 %                   |
                | False Positive Rate              | 00.15 %                   |
                | Negative Predictive Value        | 99.79 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 354612             | 541                |
                | Positive         | 742                | 95282              |
                """)   
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 355153     |
                | 1                | 0.99      | 0.99   | 0.99     | 96024      |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 451177     |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 451177     |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 451177     |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/NSD/NSD_XGBClassifier_SMOTEENN.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying SMOTEENN resampling")#, use_container_width=True
                      
        # BBBBBBBBSMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">BSMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 99.40 %                   |
                | F1 Score                         | 99.70 %                   |
                | Accuracy Score                   | 99.70 %                   |
                | Recall Score                     | 99.83 %                   |
                | Precision Score                  | 99.57 %                   |
                | ROC AUC Score                    | 99.70 %                   |
                | False Positive Rate              | 00.43 %                   |
                | Negative Predictive Value        | 99.83 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 354281             | 1711               |
                | Positive         | 596                | 356668             |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 355992     |
                | 1                | 1.00      | 1.00   | 1.00     | 357264     |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 713256     |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 713256     |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 713256     |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/NSD/NSD_XGBClassifier_BSMOTE.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying BSMOTE resampling")#, use_container_width=True
                
        # AaaaaaaaaaaaaaaaaaaaaaaaaDAaaaaaaaaaaaaaaaaaaaaaSsssssssssYyyyyNnnnn
            st.markdown('<h3 style="color: brown;">ADASYN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2) 
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performance Metrics")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 95.65 %                   |
                | F1 Score                         | 97.80 %                   |
                | Accuracy Score                   | 97.82 %                   |
                | Recall Score                     | 97.05 %                   |
                | Precision Score                  | 98.57 %                   |
                | ROC AUC Score                    | 97.82 %                   |
                | False Positive Rate              | 01.41 %                   |
                | Negative Predictive Value        | 97.08 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 351194             | 5008               |
                | Positive         | 10530              | 345897             |
                """)    
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.97      | 0.99   | 0.98     | 356202     |
                | 1                | 0.99      | 0.97   | 0.98     | 356427     |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.98     | 712629     |
                | **Macro Avg**    | 0.98      | 0.98   | 0.98     | 712629     |
                | **Weighted Avg** | 0.98      | 0.98   | 0.98     | 712629     |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/NSD/NSD_XGBClassifier_ADASYN.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying ADASYN resampling")#, use_container_width=True
      
    def Info_PS17():  
        
        if sidebar_option == "Methodology":
            Methodology()
        
        elif sidebar_option =='Dataset info':
            header()
            st.write('## PaySim 2017 Dataset (PS17)')
            st.write("""
                     
    - Content
  
        PS17 simulates mobile money transactions based on a sample of real transactions extracted from one month of financial logs of a mobile money service implemented in an African country. The original data was provided by a multinational company, which is the provider of the mobile money service currently operating in more than 14 countries around the world.
        This synthetic dataset is reduced by a quarter compared to the original dataset and has been created solely for [Kaggle](https://www.kaggle.com/datasets).

        This dataset shows transactions that took place over two days, where we have 8213 frauds out of 6354407 transactions. The dataset is highly unbalanced, with the positive class (fraud) accounting for 0.13% of all transactions.
  
        The "PS17 dataset" is a synthetic dataset that has been generated from actual financial transaction data, but which is not necessarily anonymised.
              
    - Headers

        An example of a line with the explanation :
                     
            1, PAYMENT, 1060.31, C429214117, 1089.0, 28.69, M1591654462, 0.0, 0.0, 0, 0    
              
        `step`: represents a unit of time in the real world. In this case, 1 step corresponds to 1 hour of time. The total number of steps is 744 (30-day simulation).
    	
        `type`: CASH-IN, CASH-OUT, DEBIT, PAYMENT and TRANSFER.

        `amount`: amount of the transaction in local currency.
                     
    	`nameOrig`: customer initiating the transaction.
                     
    	`oldbalanceOrg`: initial balance before the transaction.
                     
    	`newbalanceOrig`: new balance after the transaction.
                     
    	`nameDest`: customer who is the recipient of the transaction.
                     
    	`oldbalanceDest`: recipient of the initial balance before the transaction. Note that there is no information for customers beginning with M (Merchants).
                     
    	`newbalanceDest`: recipient of the new balance after the transaction. Note that there is no information for customers beginning with M (Merchants).
                     
    	`isFraud`: These are the transactions carried out by the fraudulent agents as part of the simulation. In this specific dataset, the fraudulent behaviour of the agents aims to make a profit by taking control of the customers' accounts and trying to empty the funds by transferring them to another account and then withdrawing them from the system.

        `isFlaggedFraud`: The business model aims to control massive transfers from one account to another and flags up illegal attempts. In this dataset, an illegal attempt is any attempt to transfer more than €200,000 in a single transaction.
                       
    - Previous searches

        - There are 5 similar files which contain the execution of 5 different scenarios. These files are best explained in Chapter 7 of the PhD thesis [[These]](http://urn.kb.se/resolve?urn=urn:nbn:se:bth-12932).

        - They ran ps17 multiple times using random seeds for 744 steps, representing every hour of a month of real time, which matches the original logs. Each run took around 45 minutes on an Intel i7 processor with 16GB of RAM. The final result of an execution contains around 24 million financial records divided into 5 types of category: CASH-IN, CASH-OUT, DEBIT, PAYMENT and TRANSFERS.               
                            
    Link to dataset: [See here](https://www.kaggle.com/datasets/ealaxi/paysim1)  
    """)           
       
        elif sidebar_option == "LR":
            # # Display content for Option 1
            header()
            # Display text
            st.markdown('<h3 style="color: green;">Evaluation Metrics Using LogisticRegression and different resampling methods:</h3>', unsafe_allow_html=True)

        # RUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUS
            st.markdown('<h3 style="color: brown;">RUS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)  
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performance Metrics")
                st.markdown(f"""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 91.04 %                   |
                | F1 Score                         | 95.52 %                   |
                | Accuracy Score                   | 95.52 %                   |
                | Recall Score                     | 95.03 %                   |
                | Precision Score                  | 96.02 %                   |
                | ROC AUC Score                    | 95.52 %                   |
                | False Positive Rate              | 03.99 %                   |
                | Negative Predictive Value        | 95.02 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                | Actual / Predicted |  Negative |  Positive |
                |-------------------|-----------|-----------|
                | Negative          | 1564      | 65        |
                | Positive          | 82        | 1568      |
                """)
            # Table 2: Classification Report
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support |
                |------------------|-----------|--------|----------|---------|
                | 0                | 0.95      | 0.96   | 0.96     | 1629    |
                | 1                | 0.96      | 0.95   | 0.96     | 1650    |
                |                  |           |        |          |         |
                | **Accuracy**     |           |        | 0.96     | 3279    |
                | **Macro Avg**    | 0.96      | 0.96   | 0.96     | 3279    |
                | **Weighted Avg** | 0.96      | 0.96   | 0.96     | 3279    |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/PS17/PS17_LogisticRegression_RUS.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying RUS resampling")#, use_container_width=True
            
        # ROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOS
            st.markdown('<h3 style="color: brown;">ROS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Performance Metrics
            with col1:
                st.markdown("Performance Metrics")
                st.markdown(f"""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 90.50 %                   |
                | F1 Score                         | 95.23 %                   |
                | Accuracy Score                   | 95.25 %                   |
                | Recall Score                     | 94.82 %                   |
                | Precision Score                  | 95.65 %                   |
                | ROC AUC Score                    | 95.25 %                   |
                | False Positive Rate              | 04.32 %                   |
                | Negative Predictive Value        | 94.86 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                | Actual / Predicted |  Negative |  Positive |
                |-------------------|-----------|-----------|
                | Negative          | 1214787   | 54842     |
                | Positive          | 65876     | 1206258   |
                """)
            # Table 2: Classification Report
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support |
                |------------------|-----------|--------|----------|---------|
                | 0                | 0.95      | 0.96   | 0.95     | 1269629 |
                | 1                | 0.96      | 0.95   | 0.95     | 1272134 |
                |                  |           |        |          |         |
                | **Accuracy**     |           |        | 0.95     | 2541763 |
                | **Macro Avg**    | 0.95      | 0.95   | 0.95     | 2541763 |
                | **Weighted Avg** | 0.95      | 0.95   | 0.95     | 2541763 |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/PS17/PS17_LogisticRegression_ROS.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying ROS resampling")#, use_container_width=True
            
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">SMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
           # Table 1: Performance Metrics
            with col1:
                st.markdown("Performance Metrics")
                st.markdown(f"""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 92.25%                    |
                | F1 Score                         | 96.14%                    |
                | Accuracy Score                   | 96.12%                    |
                | Recall Score                     | 96.58%                    |
                | Precision Score                  | 95.71%                    |
                | ROC AUC Score                    | 96.12%                    |
                | False Positive Rate              | 04.34%                    |
                | Negative Predictive Value        | 96.54%                    |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                | Actual / Predicted |  Negative |  Positive |
                |-------------------|-----------|-----------|
                | Negative          | 1214551   | 55078     |
                | Positive          | 43495     | 1228639   |
                """)
            # Table 2: Classification Report
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support |
                |------------------|-----------|--------|----------|---------|
                | 0                | 0.97      | 0.96   | 0.96     | 1269629 |
                | 1                | 0.96      | 0.97   | 0.96     | 1272134 |
                |                  |           |        |          |         |
                | **Accuracy**     |           |        | 0.96     | 2541763 |
                | **Macro Avg**    | 0.96      | 0.96   | 0.96     | 2541763 |
                | **Weighted Avg** | 0.96      | 0.96   | 0.96     | 2541763 |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/PS17/PS17_LogisticRegression_SMOTE.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying SMOTE resampling")#, use_container_width=True
            
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTEEEEEEEEEEEEENNNNNNNNNNNNNNNN
            st.markdown('<h3 style="color: brown;">SMOTEENN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)    
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performance Metrics")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 92.54 %                   |
                | F1 Score                         | 96.29 %                   |
                | Accuracy Score                   | 96.27 %                   |
                | Recall Score                     | 96.37 %                   |
                | Precision Score                  | 96.20 %                   |
                | ROC AUC Score                    | 96.27 %                   |
                | False Positive Rate              | 03.83 %                   |
                | Negative Predictive Value        | 96.34 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 1214808            | 48334              |
                | Positive         | 46148              | 1225259            |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 0.96      | 0.96   | 0.96     | 1263142    |
                | 1                | 0.96      | 0.96   | 0.96     | 1271407    |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.96     | 2534549    |
                | **Macro Avg**    | 0.96      | 0.96   | 0.96     | 2534549    |
                | **Weighted Avg** | 0.96      | 0.96   | 0.96     | 2534549    |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/PS17/PS17_LogisticRegression_SMOTEENN.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying SMOTEENN resampling")#, use_container_width=True
             
        # BBBBBBBBSMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">BSMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Performance Metrics
            with col1:
                st.markdown("Performance Metrics")
                st.markdown(f"""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 97.19%                    |
                | F1 Score                         | 98.60%                    |
                | Accuracy Score                   | 98.60%                    |
                | Recall Score                     | 98.56%                    |
                | Precision Score                  | 98.64%                    |
                | ROC AUC Score                    | 98.60%                    |
                | False Positive Rate              | 01.36%                    |
                | Negative Predictive Value        | 98.55%                    |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                | Actual / Predicted |  Negative |  Positive |
                |-------------------|-----------|-----------|
                | Negative          | 1252349   | 17280     |
                | Positive          | 18381     | 1253753   |
                """)
            # Table 2: Classification Report
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support |
                |------------------|-----------|--------|----------|---------|
                | 0                | 0.99      | 0.99   | 0.99     | 1269629 |
                | 1                | 0.99      | 0.99   | 0.99     | 1272134 |
                |                  |           |        |          |         |
                | **Accuracy**     |           |        | 0.99     | 2541763 |
                | **Macro Avg**    | 0.99      | 0.99   | 0.99     | 2541763 |
                | **Weighted Avg** | 0.99      | 0.99   | 0.99     | 2541763 |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/PS17/PS17_LogisticRegression_BSMOTE.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying BSMOTE resampling")#, use_container_width=True
                   
        # AaaaaaaaaaaaaaaaaaaaaaaaaDAaaaaaaaaaaaaaaaaaaaaaSsssssssssYyyyyNnnnn
            st.markdown('<h3 style="color: brown;">ADASYN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)           
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performance Metrics")
                st.markdown(f"""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 92.98%                    |
                | F1 Score                         | 96.50%                    |
                | Accuracy Score                   | 96.49%                    |
                | Recall Score                     | 96.66%                    |
                | Precision Score                  | 96.34%                    |
                | ROC AUC Score                    | 96.49%                    |
                | False Positive Rate              | 03.68%                    |
                | Negative Predictive Value        | 96.64%                    |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                | Actual / Predicted |  Negative |  Positive |
                |-------------------|-----------|-----------|
                | Negative          | 1224104   | 46716     |
                | Positive          | 42505     | 1228529   |
                """)
            # Table 2: Classification Report
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support |
                |------------------|-----------|--------|----------|---------|
                | 0                | 0.97      | 0.96   | 0.96     | 1270820 |
                | 1                | 0.96      | 0.97   | 0.96     | 1271034 |
                |                  |           |        |          |         |
                | **Accuracy**     |           |        | 0.96     | 2541854 |
                | **Macro Avg**    | 0.96      | 0.96   | 0.96     | 2541854 |
                | **Weighted Avg** | 0.96      | 0.96   | 0.96     | 2541854 |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/PS17/PS17_LogisticRegression_ADASYN.jpg", caption="The roc-auc curve and the learning curve the LR algorithm by applying ADASYN resampling")#, use_container_width=True
            
        elif sidebar_option == "DT":
            # Display content for Option 1
            header()
            # Display text
            st.markdown('<h3 style="color: green;">Evaluation Metrics Using DecisionTreeClassifier and different resampling methods:</h3>', unsafe_allow_html=True)

        # RUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUS
            st.markdown('<h3 style="color: brown;">RUS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Performance Metrics
            with col1:
                st.markdown("Performance Metrics")
                st.markdown(f"""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 97.62%                    |
                | F1 Score                         | 98.82%                    |
                | Accuracy Score                   | 98.81%                    |
                | Recall Score                     | 98.97%                    |
                | Precision Score                  | 98.67%                    |
                | ROC AUC Score                    | 98.81%                    |
                | False Positive Rate              | 1.35%                     |
                | Negative Predictive Value        | 98.95%                    |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                | Actual / Predicted |  Negative |  Positive |
                |-------------------|-----------|-----------|
                | Negative          | 1607      | 22        |
                | Positive          | 17        | 1633      |
                """)
            # Table 2: Classification Report
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support |
                |------------------|-----------|--------|----------|---------|
                | 0                | 0.99      | 0.99   | 0.99     | 1629    |
                | 1                | 0.99      | 0.99   | 0.99     | 1650    |
                |                  |           |        |          |         |
                | **Accuracy**     |           |        | 0.99     | 3279    |
                | **Macro Avg**    | 0.99      | 0.99   | 0.99     | 3279    |
                | **Weighted Avg** | 0.99      | 0.99   | 0.99     | 3279    |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/PS17/PS17_DecisionTreeClassifier_RUS.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying RUS resampling")#, use_container_width=True
            
        # ROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOS
            st.markdown('<h3 style="color: brown;">ROS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2) 
            # Table 1: Performance Metrics
            with col1:
                st.markdown("Performance Metrics")
                st.markdown(f"""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 99.98 %                   |
                | F1 Score                         | 99.99 %                   |
                | Accuracy Score                   | 99.99 %                   |
                | Recall Score                     | 100.0 %                   |
                | Precision Score                  | 99.98 %                   |
                | ROC AUC Score                    | 99.99 %                   |
                | False Positive Rate              | 00.02 %                   |
                | Negative Predictive Value        | 100.0 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                | Actual / Predicted |  Negative |  Positive |
                |--------------------|-----------|-----------|
                | Negative           | 1269402   | 227       |
                | Positive           | 0         | 1272134   |
                """)
            # Table 2: Classification Report
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support |
                |------------------|-----------|--------|----------|---------|
                | 0                | 1.00      | 1.00   | 1.00     | 1269629 |
                | 1                | 1.00      | 1.00   | 1.00     | 1272134 |
                |                  |           |        |          |         |
                | **Accuracy**     |           |        | 1.00     | 2541763 |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 2541763 |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 2541763 |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/PS17/PS17_DecisionTreeClassifier_ROS.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying ROS resampling")#, use_container_width=True
            
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">SMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Performance Metrics
            with col1:
                st.markdown("Performance Metrics")
                st.markdown(f"""
                | Metric                           | Score                      |
                |----------------------------------|----------------------------|
                | Matthews Correlation Coefficient | 99.89 %                    |
                | F1 Score                         | 99.95 %                    |
                | Accuracy Score                   | 99.95 %                    |
                | Recall Score                     | 99.97 %                    |
                | Precision Score                  | 99.92 %                    |
                | ROC AUC Score                    | 99.95 %                    |
                | False Positive Rate              | 00.08 %                    |
                | Negative Predictive Value        | 99.97 %                    |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                | Actual / Predicted |  Negative |  Positive |
                |--------------------|-----------|-----------|
                | Negative           | 1268667   | 962       |
                | Positive           | 419       | 1271715   |
                """)
            # Table 2: Classification Report
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support |
                |------------------|-----------|--------|----------|---------|
                | 0                | 1.00      | 1.00   | 1.00     | 1269629 |
                | 1                | 1.00      | 1.00   | 1.00     | 1272134 |
                |                  |           |        |          |         |
                | **Accuracy**     |           |        | 1.00     | 2541763 |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 2541763 |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 2541763 |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/PS17/PS17_DecisionTreeClassifier_SMOTE.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying SMOTE resampling")#, use_container_width=True
            
        
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTEEEEEEEEEEEEENNNNNNNNNNNNNNNN
            st.markdown('<h3 style="color: brown;">SMOTEENN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performance Metrics")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 99.90 %                   |
                | F1 Score                         | 99.95 %                   |
                | Accuracy Score                   | 99.95 %                   |
                | Recall Score                     | 99.97 %                   |
                | Precision Score                  | 99.93 %                   |
                | ROC AUC Score                    | 99.95 %                   |
                | False Positive Rate              | 00.07 %                   |
                | Negative Predictive Value        | 99.97 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 1262234            | 908                |
                | Positive         | 340                | 1271067            |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 1263142    |
                | 1                | 1.00      | 1.00   | 1.00     | 1271407    |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.99     | 2534549    |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 2534549    |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 2534549    |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/PS17/PS17_DecisionTreeClassifier_SMOTEENN.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying SMOTEENN resampling")#, use_container_width=True
         
        # BBBBBBBBSMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">BSMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 99.94 %                   |
                | F1 Score                         | 99.97 %                   |
                | Accuracy Score                   | 99.97 %                   |
                | Recall Score                     | 99.98 %                   |
                | Precision Score                  | 99.95 %                   |
                | ROC AUC Score                    | 99.97 %                   |
                | False Positive Rate              | 00.05 %                   |
                | Negative Predictive Value        | 99.98 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 1269050            | 579                |
                | Positive         | 241                | 1271893            |
                """)  
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 1269629    |
                | 1                | 1.00      | 1.00   | 1.00     | 1272134    |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 2541763    |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 2541763    |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 2541763    |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/PS17/PS17_DecisionTreeClassifier_BSMOTE.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying BSMOTE resampling")#, use_container_width=True
            
        # AaaaaaaaaaaaaaaaaaaaaaaaaDAaaaaaaaaaaaaaaaaaaaaaSsssssssssYyyyyNnnnn
            st.markdown('<h3 style="color: brown;">ADASYN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 99.90 %                   |
                | F1 Score                         | 99.95 %                   |
                | Accuracy Score                   | 99.95 %                   |
                | Recall Score                     | 99.98 %                   |
                | Precision Score                  | 99.93 %                   |
                | ROC AUC Score                    | 99.95 %                   |
                | False Positive Rate              | 00.07 %                   |
                | Negative Predictive Value        | 99.98 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 1269880            | 940                |
                | Positive         | 315                | 1270719            |
                """)               
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 1270820    |
                | 1                | 1.00      | 1.00   | 1.00     | 1271034    |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 2541854    |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 2541854    |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 2541854    |
                """)

            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/PS17/PS17_DecisionTreeClassifier_ADASYN.jpg", caption="The roc-auc curve and the learning curve the DT algorithm by applying ADASYN resampling")#, use_container_width=True

        elif sidebar_option == "RF":
            # Display content for Option 1
            header()
            # Display text
            st.markdown('<h3 style="color: green;">Evaluation Metrics Using RandomForestClassifier and different resampling methods:</h3>', unsafe_allow_html=True)

        # RUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUS
            st.markdown('<h3 style="color: brown;">RUS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 98.60 %                   |
                | F1 Score                         | 99.30 %                   |
                | Accuracy Score                   | 99.30 %                   |
                | Recall Score                     | 99.58 %                   |
                | Precision Score                  | 99.04 %                   |
                | ROC AUC Score                    | 99.30 %                   |
                | False Positive Rate              | 00.98 %                   |
                | Negative Predictive Value        | 99.57 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 1613               | 16                 |
                | Positive         | 7                  | 1643               |
                """) 
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 0.99   | 0.99     | 1629       |
                | 1                | 0.99      | 1.00   | 0.99     | 1650       |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.99     | 3279       |
                | **Macro Avg**    | 0.99      | 0.99   | 0.99     | 3279       |
                | **Weighted Avg** | 0.99      | 0.99   | 0.99     | 3279       |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/PS17/PS17_RandomForestClassifier_RUS.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying RUS resampling")#, use_container_width=True
            
        # ROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOS
            st.markdown('<h3 style="color: brown;">ROS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 99.99 %                   |
                | F1 Score                         | 99.99 %                   |
                | Accuracy Score                   | 99.99 %                   |
                | Recall Score                     | 100.0 %                   |
                | Precision Score                  | 99.99 %                   |
                | ROC AUC Score                    | 99.99 %                   |
                | False Positive Rate              | 00.00 %                   |
                | Negative Predictive Value        | 100.0 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 1269566            | 63                 |
                | Positive         | 0                  | 1272134            |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 1269629    |
                | 1                | 1.00      | 1.00   | 1.00     | 1272134    |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 2541763    |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 2541763    |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 2541763    |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/PS17/PS17_RandomForestClassifier_ROS.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying ROS resampling")#, use_container_width=True
            
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">SMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 99.92 %                   |
                | F1 Score                         | 99.96 %                   |
                | Accuracy Score                   | 99.96 %                   |
                | Recall Score                     | 99.99 %                   |
                | Precision Score                  | 99.92 %                   |
                | ROC AUC Score                    | 99.96 %                   |
                | False Positive Rate              | 00.08 %                   |
                | Negative Predictive Value        | 99.99 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 1268661            | 968                |
                | Positive         | 56                 | 1272078            |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 1269629    |
                | 1                | 1.00      | 1.00   | 1.00     | 1272134    |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 2541763    |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 2541763    |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 2541763    |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/PS17/PS17_RandomForestClassifier_SMOTE.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying SMOTE resampling")#, use_container_width=True
            
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTEEEEEEEEEEEEENNNNNNNNNNNNNNNN
            st.markdown('<h3 style="color: brown;">SMOTEENN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performance Metrics")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 99.93 %                   |
                | F1 Score                         | 99.97 %                   |
                | Accuracy Score                   | 99.97 %                   |
                | Recall Score                     | 99.99 %                   |
                | Precision Score                  | 99.93 %                   |
                | ROC AUC Score                    | 99.96 %                   |
                | False Positive Rate              | 00.07 %                   |
                | Negative Predictive Value        | 99.99 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 1262283            | 859                |
                | Positive         | 26                 | 1271381            |
                """) 
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 1263142    |
                | 1                | 1.00      | 1.00   | 1.00     | 1271407    |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 2534549    |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 2534549    |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 2534549    |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/PS17/PS17_RandomForestClassifier_SMOTEENN.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying SMOTEENN resampling")#, use_container_width=True
    
        # BBBBBBBBSMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">BSMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performance Metrics")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 99.97 %                   |
                | F1 Score                         | 99.98 %                   |
                | Accuracy Score                   | 99.98 %                   |
                | Recall Score                     | 99.99 %                   |
                | Precision Score                  | 99.98 %                   |
                | ROC AUC Score                    | 99.98 %                   |
                | False Positive Rate              | 00.02 %                   |
                | Negative Predictive Value        | 99.99 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 1269398            | 231                |
                | Positive         | 189                | 1271945            |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 1269629    |
                | 1                | 1.00      | 1.00   | 1.00     | 1272134    |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 2541763    |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 2541763    |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 2541763    |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/PS17/PS17_RandomForestClassifier_BSMOTE.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying BSMOTE resampling")#, use_container_width=True
            
        # AaaaaaaaaaaaaaaaaaaaaaaaaDAaaaaaaaaaaaaaaaaaaaaaSsssssssssYyyyyNnnnn
            st.markdown('<h3 style="color: brown;">ADASYN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)           
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performance Metrics")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 99.92 %                   |
                | F1 Score                         | 99.96 %                   |
                | Accuracy Score                   | 99.96 %                   |
                | Recall Score                     | 99.99 %                   |
                | Precision Score                  | 99.92 %                   |
                | ROC AUC Score                    | 99.96 %                   |
                | False Positive Rate              | 00.08 %                   |
                | Negative Predictive Value        | 99.99 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 1269803            | 1017               |
                | Positive         | 14                 | 1271020            |
                """)  
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 1270820    |
                | 1                | 1.00      | 1.00   | 1.00     | 1271034    |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.99     | 2541854    |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 2541854    |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 2541854    |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/PS17/PS17_RandomForestClassifier_ADASYN.jpg", caption="The roc-auc curve and the learning curve the RF algorithm by applying ADASYN resampling")#, use_container_width=True
            
        elif sidebar_option == "XGB":
            # Display content for Option 2
            header()                       
            # Display text
            st.markdown('<h3 style="color: green;">Evaluation Metrics Using XGBClassifier and different resampling methods:</h3>', unsafe_allow_html=True)

        # RUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUS
            st.markdown('<h3 style="color: brown;">RUS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 98.78 %                   |
                | F1 Score                         | 99.40 %                   |
                | Accuracy Score                   | 99.39 %                   |
                | Recall Score                     | 99.64 %                   |
                | Precision Score                  | 99.16 %                   |
                | ROC AUC Score                    | 99.39 %                   |
                | False Positive Rate              | 00.86 %                   |
                | Negative Predictive Value        | 99.63 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 1615               | 14                 |
                | Positive         | 6                  | 1644               |
                """)              
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 0.99   | 0.99     | 1629       |
                | 1                | 0.99      | 1.00   | 0.99     | 1650       |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.99     | 3279       |
                | **Macro Avg**    | 0.99      | 0.99   | 0.99     | 3279       |
                | **Weighted Avg** | 0.99      | 0.99   | 0.99     | 3279       |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/PS17/PS17_XGBClassifier_RUS.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying RUS resampling")#, use_container_width=True
            
        # ROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOS
            st.markdown('<h3 style="color: brown;">ROS method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)          
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 99.87 %                   |
                | F1 Score                         | 99.94 %                   |
                | Accuracy Score                   | 99.94 %                   |
                | Recall Score                     | 100.0 %                   |
                | Precision Score                  | 99.87 %                   |
                | ROC AUC Score                    | 99.94 %                   |
                | False Positive Rate              | 00.13 %                   |
                | Negative Predictive Value        | 100.0 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 1267997            | 1632               |
                | Positive         | 0                  | 1272134            |
                """)                
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 1269629    |
                | 1                | 1.00      | 1.00   | 1.00     | 1272134    |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 2541763    |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 2541763    |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 2541763    |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/PS17/PS17_XGBClassifier_ROS.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying ROS resampling")#, use_container_width=True
            

        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">SMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)        
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performances metric")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 99.70 %                   |
                | F1 Score                         | 99.85 %                   |
                | Accuracy Score                   | 99.85 %                   |
                | Recall Score                     | 99.91 %                   |
                | Precision Score                  | 99.79 %                   |
                | ROC AUC Score                    | 99.85 %                   |
                | False Positive Rate              | 00.20 %                   |
                | Negative Predictive Value        | 99.91 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 1267009            | 2620               |
                | Positive         | 1189               | 1270945            |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 1269629    |
                | 1                | 1.00      | 1.00   | 1.00     | 1272134    |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 2541763    |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 2541763    |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 2541763    |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/PS17/PS17_XGBClassifier_SMOTE.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying SMOTE resampling")#, use_container_width=True
            
        
        # SMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTEEEEEEEEEEEEENNNNNNNNNNNNNNNN
            st.markdown('<h3 style="color: brown;">SMOTEENN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performance Metrics")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 99.77 %                   |
                | F1 Score                         | 99.88 %                   |
                | Accuracy Score                   | 99.88 %                   |
                | Recall Score                     | 99.93 %                   |
                | Precision Score                  | 99.84 %                   |
                | ROC AUC Score                    | 99.88 %                   |
                | False Positive Rate              | 00.16 %                   |
                | Negative Predictive Value        | 99.93 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 1261116            | 2026               |
                | Positive         | 928                | 1270479            |
                """)   
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 1263142    |
                | 1                | 1.00      | 1.00   | 1.00     | 1271407    |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 2534549    |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 2534549    |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 2534549    |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/PS17/PS17_XGBClassifier_SMOTEENN.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying SMOTEENN resampling")#, use_container_width=True
                      
        # BBBBBBBBSMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE
            st.markdown('<h3 style="color: brown;">BSMOTE method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2)
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performance Metrics")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 99.91 %                   |
                | F1 Score                         | 99.96 %                   |
                | Accuracy Score                   | 99.96 %                   |
                | Recall Score                     | 99.99 %                   |
                | Precision Score                  | 99.92 %                   |
                | ROC AUC Score                    | 99.96 %                   |
                | False Positive Rate              | 00.08 %                   |
                | Negative Predictive Value        | 99.99 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 1268581            | 1048               |
                | Positive         | 66                 | 1272068            |
                """)                
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 1269629    |
                | 1                | 1.00      | 1.00   | 1.00     | 1272134    |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 1.00     | 2541763    |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 2541763    |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 2541763    |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/PS17/PS17_XGBClassifier_BSMOTE.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying BSMOTE resampling")#, use_container_width=True
                
        # AaaaaaaaaaaaaaaaaaaaaaaaaDAaaaaaaaaaaaaaaaaaaaaaSsssssssssYyyyyNnnnn
            st.markdown('<h3 style="color: brown;">ADASYN method: </h3>', unsafe_allow_html=True)
            st.subheader("Evaluation Metrics")
            # Create three columns
            col1, col2 = st.columns(2) 
            # Table 1: Evaluation Metrics
            with col1:
                st.markdown("Performance Metrics")
                st.markdown("""
                | Metric                           | Score                     |
                |----------------------------------|---------------------------|
                | Matthews Correlation Coefficient | 99.67 %                   |
                | F1 Score                         | 99.83 %                   |
                | Accuracy Score                   | 99.83 %                   |
                | Recall Score                     | 99.92 %                   |
                | Precision Score                  | 99.75 %                   |
                | ROC AUC Score                    | 99.83 %                   |
                | False Positive Rate              | 00.25 %                   |
                | Negative Predictive Value        | 99.92 %                   |
                """)
                st.markdown("Confusion Matrix")
                st.markdown("""
                |Actual / Predicted|  Negative          |  Positive          |
                |------------------|--------------------|--------------------|
                | Negative         | 1267643            | 3177               |
                | Positive         | 1071               | 1269963            |
                """)
            # Table 2: Confusion Matrix
            with col2:
                st.markdown("Classification Report")
                st.markdown("""
                |                  | Precision | Recall | F1 Score | Support    |
                |------------------|-----------|--------|----------|------------|
                | 0                | 1.00      | 1.00   | 1.00     | 1270820    |
                | 1                | 1.00      | 1.00   | 1.00     | 1271034    |
                |                  |           |        |          |            |
                | **Accuracy**     |           |        | 0.99     | 2541854    |
                | **Macro Avg**    | 1.00      | 1.00   | 1.00     | 2541854    |
                | **Weighted Avg** | 1.00      | 1.00   | 1.00     | 2541854    |
                """)
            # Display a local image
            st.subheader("ROC-AUC & Learning curve")
            image = st.image("Figs/PS17/PS17_XGBClassifier_ADASYN.jpg", caption="The roc-auc curve and the learning curve the XGB algorithm by applying ADASYN resampling")#, use_container_width=True
    
    # Define function to choose dataset and call corresponding user input function
    def choose_dataset():
        dataset_choice = st.sidebar.radio("Select Dataset", ['Credit-Card Dataset', 'Alice Dataset', 'IEEE dataset', 'LOAN dataset', 
                                                             'NSD dataset', 'PaySim17 dataset'])
        if dataset_choice   == 'Credit-Card Dataset':
            Info_CC()
        elif dataset_choice == 'Alice Dataset':
            Info_CMIYC()
        elif dataset_choice == 'IEEE dataset':
            Info_IEEE()
        elif dataset_choice == 'LOAN dataset':
            Info_LOAN()
        elif dataset_choice == 'NSD dataset':
            Info_NSD()
        else:
            Info_PS17()
            
    choose_dataset()

# Create a function to display the user guide 
def display_user_guide():
    col1, col2  = st.columns([3, 1])
    with col1:
        st.markdown("""<h3 style='color: orange;'>HADDOU Khalid</h3>""", unsafe_allow_html=True)
    with col2:
        st.markdown("<h3 style='color: green;'>GrassFields</h3>", unsafe_allow_html=True)
        st.image('GF_logo/GRASSFIELDS_LogoBG.png', width=150)

    # Create a centered container
    widget_container = st.container()
    with widget_container:
        st.markdown("#  Introduction")
        st.write("""
                    Welcome to User Guide of the web application for predicting transaction types (Fraud, Non-Fraud)
                    using different machine learning algorithms including Logistic Regression, Decision Tree, Random Forest, and XGBoost, and 6 different datasets including Credit-Card Dataset (CC), Alice Dataset (CMIYC), IEEE dataset (IEEE), LOAN dataset (LOAN), New Simulated Data dataset (NSD), PaySim-2017 dataset (PS17) (detailed on the info page).
                    This guide will help you navigate through the application's features and understand how to use it effectively.""") 
        st.markdown("# I - Application Structure")
        st.markdown("The application is organized into two main sections:")
        st.markdown("""
                    ## 1. Main Page

                    This page allows you to make predictions using different datasets and various machine learning models displayed on the lift sidebar. 
                    Each model corresponds to a different algorithm. The available models are:
                    Logistic Regression (LR), Decision Tree (DT), Random Forest (RF), XGBoost (XGB)
                    """)
        st.markdown("""
                    Here's how the Main Page is structured:

                        Model Selection: 
                            Use the radio buttons in the sidebar to select the desired machine learning algorithm.
                        
                        Dataset Selection: 
                            Use the radio buttons in the sidebar to select the desired Dataset. A link to the dataset is provided for each selected one.
                    
                        Input Options:
                            Upload CSV File: You can upload a CSV file containing transaction data for testing and prediction.
                            Manual Input: Alternatively, you can manually input feature values using sliders in the sidebar.
                        
                        Display of User Input: 
                            Any features you provide (either via CSV upload or manual input) will be displayed on the page.

                        Prediction Results: 
                            Once the model is selected, it uses pre-trained models to predict transaction types based on the provided input. 
                            The predictions and their probabilities are displayed in two separate columns.

                    """)
        st.markdown("""
                    ## 2. Info Page
                    
                    The Info Page provides detailed information about the model building process, as well as the evaluation metrics for each algorithm on various datasets. 
                    It includes the following details:                    

                        Model Details: 
                            Information about how the models were built and trained.
                    
                        Evaluation Metrics: 
                            Details about various evaluation metrics, including ROC-AUC curve and learning curve. 
                            Special attention is given to metrics that are well-suited for handling imbalanced data.
                    
                    """)
        st.markdown("""
            # II - Using the Application
            
                1 - Selecting a Model:
                    On the Main Page, use the radio buttons in the sidebar to choose the machine learning algorithm you want to use (Logistic Regression (LR), Decision Tree (DT), Random Forest (RF) or XGBoost (XGB)).
        
                2 - Selecting a Dataset:
                    On the Main Page, use the radio buttons in the sidebar to choose the dataset you want to use (Credit-Card Dataset, Alice Dataset, IEEE dataset, LOAN dataset, NSD dataset, PaySim17 dataset).
            
                2 - Input Options:
                    Upload CSV File:
                        Click on the "Upload CSV File" option. Upload a CSV file containing the transaction data you want to test and predict.
                    Manual Input:
                        Use the sliders in the sidebar to manually input feature values.
            
                3 - Display of User Input:
                    Any features you provide will be displayed on the page.
            
                4 - Viewing Predictions:
                    The selected model will use the provided input to make predictions about the transaction types. The predictions and their probabilities will be displayed in two separate columns.
            
                5 - Accessing Additional Information:
                    Navigate to the Info Page to get detailed insights about the model building process, evaluation metrics, ROC-AUC curves, and learning curves.

            """)


# Create a sidebar with navigation
st.sidebar.title("Menu")
selection = st.sidebar.selectbox("Go to", [ "Test", "Info", "User Guide"])

# Conditional rendering based on user selection
if selection == "Test":
    Test()
elif selection == "Info":
    Info()
elif selection == "User Guide":
    display_user_guide()
