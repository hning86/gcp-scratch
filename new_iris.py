 # Initialize and train the Logistic Regression model
 print("Training the model...")
 model = LogisticRegression(max_iter=200)
 model.fit(X_train_scaled, y_train)

 # 5. Evaluate the model on the test set
 y_pred = model.predict(X_test_scaled)
 accuracy = accuracy_score(y_test, y_pred)

 print(f"\nModel Accuracy: {accuracy * 100:.2f}%\n")
 print("Classification Report:")
 print(classification_report(y_test, y_pred, target_names=iris.target_names))

 # 6. Save the model and scaler for future predictions
 joblib.dump(model, 'iris_model.joblib')
 joblib.dump(scaler, 'iris_scaler.joblib')
 print("Model and scaler saved successfully as 'iris_model.joblib' and 'iris_scaler.joblib'")
 
